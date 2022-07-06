from flask import Flask
from threading import Thread
from os import getenv

app = Flask('')

@app.route('/')
def main():
  return "<strong><p style=\"font-family:'Consolas'\">Your bot is alive!</p></strong>"


def run():
  app.run(host="0.0.0.0", port=getenv("PORT"))

def keep_alive():
  server = Thread(target=run)
  server.start()

