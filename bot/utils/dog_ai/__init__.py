import os

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

start_sequence = "\nA:"
restart_sequence = "\n\nQ: "
training_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "prompt_base.txt"))


def get_response(message: str) -> str:
    # read training dataset and append user question/message
    with open(file=training_file, mode="r") as file:  # ToDo: use a 2nd file (uncommitted) for expanding dataset
        training = file.read()
    training = training.replace("__MESSAGE__", message)

    # fetch response to message from GPT-3
    response = openai.Completion.create(
        engine="davinci",
        prompt=training,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        presence_penalty=0.6,
        stop=["\n", "Q:", "A:"]
    )
    response = response.get("choices")[0].get("text")

    # allow dataset to grow i.e. learn
    training += response
    training += "\n\nQ: __MESSAGE__\nA:"
    with open(file=training_file, mode="w") as file:
        file.write(training)

    return response
