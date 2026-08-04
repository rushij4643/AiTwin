from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv
import gradio as gr
import os

load_dotenv(override=True)

MODEL_NAME = "gemini-3.1-flash-lite"

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def chat(message, history):

    messages = system + history + [{"role": "user", "content": message}]

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            tools=tools,
            temperature=0.4
        )

        while response.choices[0].finish_reason == "tool_calls":

            assistant_message = response.choices[0].message
            tool_calls = assistant_message.tool_calls

            results = handle_tool_calls(tool_calls)

            messages.append(assistant_message)
            messages.extend(results)

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                tools=tools,
                temperature=0.4
            )

        content = response.choices[0].message.content

        if not content:
            content = "I'm sorry, I couldn't generate a response."

        return content

    except Exception as e:
        print(f"Error: {e}")
        return f"⚠️ Error: {str(e)}"


if __name__ == "__main__":

    gr.ChatInterface(
        fn=chat,
        examples=EXAMPLES,
        title="AI Digital Twin",
        description="Ask me anything about my background, skills, experience and projects.",
        chatbot=gr.Chatbot(show_label=False),
    ).launch(
        css=CSS,
        js=JS,
        theme=gr.themes.Base()
    )