import os

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

start_sequence = "\nA:"
restart_sequence = "\n\nQ: "


def get_response(message: str) -> str:
    with open(file="bot\\utils\\dog_ai\\prompt_base.txt", mode="r") as file:  # TODO: make relative path
        training = file.read()
        training = training.replace("__MESSAGE__", message)

    response = openai.Completion.create(
        engine="davinci",
        prompt=training,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        presence_penalty=0.6,
        stop=["\n", "Q:", "A:"]
    )
    return response.get("choices")[0].get("text")
