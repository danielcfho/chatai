import openai
import gradio as gr
import os
from gtts import gTTS
import subprocess
import tempfile
import dotenv
dotenv.load_dotenv()
from pygame import mixer

openai.api_key = os.getenv('OPENAI_API_KEY')

prompt = "I want you to act as an English translator, spelling corrector and improver. I will speak to you in any language and you will detect the language, translate it and answer in the corrected and improved version of my text, in English. I want you to replace my simplified A0-level words and sentences with more beautiful and elegant, upper level English words and sentences. Keep the meaning same, but make them more colloquial. I want you to only reply the correction, the improvements and nothing else, do not write explanations. My first sentence is '你好嗎？'"

messages=[
  {"role":"system","content": prompt},
]

def say(text,filename=None):
  with tempfile.NamedTemporaryFile(delete=True) as temp:
    tts = gTTS(text=text,lang='en',slow=False)
    if filename is None:
      filename = f'{temp.name}.mp3'
    print(os.path.abspath(filename))
    tts.save(filename)
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    while mixer.music.get_busy():
      continue
    mixer.quit()

def transcribe(audio):
  global messages

  audio_file = open(audio, 'rb')
  print(audio_file)
  transcript = openai.Audio.transcribe('whisper-1',audio_file)
  print(transcript['text'])

  messages.append({"role":"user","content":transcript['text']})
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
  )

  system_message = response['choices'][0]['message']['content']
  # say(system_message,"system.mp3")
  # subprocess.call(['say', system_message, '-o', 'system.aiff'])
  # subprocess.call(['ffmpeg','-y','-i', 'system.aiff', '-acodec', 'pcm_s16le', '-ac', '1', '-ar', '16000', 'system.wav'])
  subprocess.call(['say', system_message])

  messages.append({"role":"assistant","content":system_message})

  chat_transcript = ""
  for msg in messages:
    if msg['role'] != 'system':
      chat_transcript += f'{msg["role"]}: {msg["content"]}\n\n'

  return chat_transcript

ui = gr.Interface(
  fn=transcribe,
  inputs=gr.Audio(source="microphone", type="filepath"),
  # outputs=[gr.Audio('system.wav'),"text"],
  outputs='text',
  live=True,
)

ui.launch()