from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai



load_dotenv()
apen.api_key = os.getenv("OPEN_API_KEY")
completion = openai.Completion()

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
prompt_text = f'(chat_log)(restart_sequence)'
  model="text-davinci-002",
  prompt= 
  temperature=0.9,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.59
)