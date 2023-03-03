import os
from dotenv import load_dotenv
import openai
load_dotenv()

PROMPT_TEACH_ENG='''
I want you to act as an English translator, spelling corrector and improver. I will speak to you in any language and you will detect the language, translate it and answer in the corrected and improved version of my text, in English. I want you to replace my simplified A0-level words and sentences with more beautiful and elegant, upper level English words and sentences. Keep the meaning same, but make them more literary. I want you to write explanations. My first sentence is "你好嗎？"'''

openai.api_key = os.getenv('OPENAI_API_KEY')

messages = []
# system_msg = input("what type of chatbot would you like to use?\n")
system_msg = PROMPT_TEACH_ENG
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