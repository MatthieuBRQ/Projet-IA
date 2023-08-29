import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot_reponse(prompt):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      temperature=0.5,
      max_tokens=100
    )
    return response.choices[0].text.strip()

while True:
    prompt = input("Vous: ")
    print("ChatBot: ", chatbot_reponse(prompt))

