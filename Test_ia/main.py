import os
import openai
import pyttsx3

openai.api_key = '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'
engine = pyttsx3.init()
# La vitesse de la voix
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)     # Modifie la vitesse de la voix. Plus le nombre est bas, plus la voix est lente.

# Volume de la voix
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)    # Modifie le volume de la voix. La valeur doit être comprise entre 0 et 1.

def chatbot_reponse(prompt, conversation_history):
    conversation_history += f"Vous: {prompt}\n"

    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=conversation_history,
      temperature=0.5,
      max_tokens=100
    )

    conversation_history += f"ChatBot: {response.choices[0].text.strip()}\n"
    return response.choices[0].text.strip(), conversation_history

while True:
    conversation_history = ""
    prompt = input("Vous: ")
    bot_response, conversation_history = chatbot_reponse(prompt, conversation_history)
    print("ChatBot: ", bot_response)
    engine.say(bot_response)
    engine.runAndWait()

