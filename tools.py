import json
import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

# -----------------------------
# Pushover Configuration
# -----------------------------
pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")

PUSHOVER_URL = "https://api.pushover.net/1/messages.json"


def push(message):
    """
    Send a push notification using Pushover.
    """
    if not pushover_user or not pushover_token:
        print("Pushover credentials not configured.")
        return

    try:
        requests.post(
            PUSHOVER_URL,
            data={
                "token": pushover_token,
                "user": pushover_user,
                "message": message,
            },
            timeout=10,
        )
    except Exception as e:
        print(f"Pushover Error: {e}")


# -----------------------------
# Record User Details
# -----------------------------
def record_user_details(email, name="Name not provided", notes="Not provided"):
    """
    Save the visitor's email into emails.txt
    and send a Pushover notification.
    """

    try:
        with open("emails.txt", "a", encoding="utf-8") as f:
            f.write(email.strip() + "\n")

        print(f"Recorded email: {email}")

    except Exception as e:
        print(f"Error saving email: {e}")

    push(
        f"📩 New Digital Twin Contact\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Notes: {notes}"
    )

    return "OK"


# -----------------------------
# Record Unknown Question
# -----------------------------
def record_unknown_question(question):
    push(
        f"❓ Unknown Question\n\n"
        f"{question}"
    )

    return "OK"


# -----------------------------
# Tool Definitions
# -----------------------------
record_user_details_json = {
    "name": "record_user_details",
    "description": "Use this tool whenever the visitor provides their email address and wants to get in touch.",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {
                "type": "string",
                "description": "Visitor email address",
            },
            "name": {
                "type": "string",
                "description": "Visitor name",
            },
            "notes": {
                "type": "string",
                "description": "Extra notes about the conversation",
            },
        },
        "required": ["email"],
        "additionalProperties": False,
    },
}

record_unknown_question_json = {
    "name": "record_unknown_question",
    "description": "Record a question that the AI could not answer.",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "Question that couldn't be answered",
            }
        },
        "required": ["question"],
        "additionalProperties": False,
    },
}

tools = [
    {
        "type": "function",
        "function": record_user_details_json,
    },
    {
        "type": "function",
        "function": record_unknown_question_json,
    },
]

tool_map = {
    "record_user_details": record_user_details,
    "record_unknown_question": record_unknown_question,
}


# -----------------------------
# Handle Tool Calls
# -----------------------------
def handle_tool_calls(tool_calls):
    results = []

    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print(f"Tool called: {tool_name}")

        tool = tool_map.get(tool_name)

        if tool:
            result = tool(**arguments)
        else:
            result = f"Unknown tool: {tool_name}"

        results.append(
            {
                "role": "tool",
                "content": json.dumps(result),
                "tool_call_id": tool_call.id,
            }
        )

    return results