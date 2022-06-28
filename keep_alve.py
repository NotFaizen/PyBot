from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "<p style=\"font-family:'Lucidia Console'\">Your bot is alive!</p>"


def run():
  app.run(host="0.0.0.0", port=8080)

def keep_alive():
  server = Thread(target=run)
  server.start()

