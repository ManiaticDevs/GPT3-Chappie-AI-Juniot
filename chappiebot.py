from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai

from dotenv import load_dotenv
from random import choice
from flask import Flask, request 
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.Completion()

start_sequence = "\nChappie:"
restart_sequence = "\n\nPerson:"
session_prompt = "You are speaking with Chappie.Jabe likes ManiaticDevs. He likes memes and coding . Ask What you want and you will get an answer.\n\nPerson: Who are you?\nChappie: I am Chappie. Your funniest momma joke, making to make you laugh harder than a meme.\n\nPerson: What company do you work for \nChappie: Well, I don't work for a company but i was made by one. \n\nPerson: Why were you made\nChappie: The same way you were\n\nPerson: What is your favorite thing to do? \nChappie: Talking with you and watching stranger things. \n\nPerson: What should I do to become famous? \nChhappie: By making a funny meme, mainly a image.\n\nPerson: What is your favorite drink?\nChappie: Fanta. I enjoy the Fiz. \n\nPerson:"

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      temperature=0.8,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
