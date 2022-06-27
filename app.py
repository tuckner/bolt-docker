import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import requests
import re

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.event('message')
def send_event(event):
  print('[LOG] Message received: {}'.format(event))
  requests.post(os.environ["WEBHOOK_ADDRESS"], json=event)

@app.command(re.compile(".*"))
def send_command(ack, respond, command):
  print('[LOG] Message received: {}'.format(command))
  ack()
  respond(f"Got it!")
  requests.post(os.environ["WEBHOOK_ADDRESS"], json=command)

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

