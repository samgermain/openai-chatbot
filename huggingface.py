# huggingface.co/models

from transformers import pipeline, Conversation
import gradio as gr

# toy example 2
classifier = pipeline(
    task="sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

print(classifier("Love this!"))

message_list = []
response_list = []

chatbot = pipeline(model="facebook/blenderbot-400M-distill")


def vanilla_chatbot(message, history):
    conversation = Conversation(
        text=message,
        past_user_inputs=message_list,
        generative_response=response_list
    )
    conversation = chatbot(conversation)

    return conversation.generated_responses[-1]


demo_chatbot = gr.ChatInterface(
    vanilla_chatbot,
    title="Vanilla Chatbot",
    description="Enter text to start chatting",
)

demo_chatbot.launch()
