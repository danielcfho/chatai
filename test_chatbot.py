import unittest
from dotenv import load_dotenv
import os
import openai

class TestChatbot(unittest.TestCase):
  def setUp(self):
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')
    self.messages = []
    self.system_msg = input("what type of chatbot would you like to use?\n")
    self.messages.append({"role":"system","content":self.system_msg})
    print("Say hello")
  
  def test_happy_path(self):
    message = "Hello"
    self.messages.append({"role":"user","content":message})
    response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages=self.messages)
    reply = response["choices"][0]["message"]["content"]
    self.messages.append({"role":"user","content":reply})
    self.assertNotEqual(reply, "")
  
  def test_empty_input(self):
    message = ""
    self.messages.append({"role":"user","content":message})
    response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages=self.messages)
    reply = response["choices"][0]["message"]["content"]
    self.messages.append({"role":"user","content":reply})
    self.assertNotEqual(reply, "")
  
  def test_quit_input(self):
    message = "quit()"
    self.messages.append({"role":"user","content":message})
    response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages=self.messages)
    reply = response["choices"][0]["message"]["content"]
    self.messages.append({"role":"user","content":reply})
    self.assertEqual(reply, "")

if __name__ == '__main__':
  unittest.main()