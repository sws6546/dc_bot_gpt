import openai
from envVars import openaiKey

def answerGpt(question):
    openai.organization = "org-Lmrqm7P0pOMvYXbB7UFneZt3"
    openai.api_key = openaiKey

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "user", "content" : question}
        ]
    )
    return completion.choices[0].message.content

