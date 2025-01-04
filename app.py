import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.message("hello")
def message_hello(message, say):
    user = message['user']
    say(
      blocks=[
        {
          "type": "section",
          "text": { "type": "mrkdwn", "text": f"Hey there <@{user}>!" },
          "accessory": {
            "type": "button",
            "text": { "type": "plain_text", "text": "Click Me" },
            "action_id": "button_click"
          }
        }
      ],
      text=f"Hey there <@{user}>!"
    )

@app.action("button_click")
def action_button_click(body, ack, say):
    ack()
    say(f"<@{body['user']['id']}> clicked the button!")

if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
