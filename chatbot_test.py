import os
from dotenv import load_dotenv
import openai
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

messages = []
system_msg = input("what type of chatbot would you like to use?\n")
messages.append({"role":"system","content":system_msg})

print("Say hello")
while ( message := input('') ) != 'quit()':
  messages.append({"role":"user","content":message})
  response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=messages)
  reply = response["choices"][0]["message"]["content"]
  messages.append({"role":"user","content":reply})
  print("\n" + reply + "\n")