import os
from typing import List
import requests
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.command('/dajare')
def dajare_command_handler(ack, body, say, respond, client):
  ack()

  user_id = body['user_id']
  text_input = body['text']

  respond('駄洒落を生成中...')

  try:
    dajare_texts = get_dajare(text_input)

    dm_channel = client.conversations_open(users=user_id)
    channel_id = dm_channel['channel']['id']

    say(
      text=f'<@{user_id}> さん、生成された駄洒落から選択してください:',
      blocks=[
        generate_dajare_select_block(dajare_texts),
      ],
      channel=channel_id
    )
    respond('生成した駄洒落をDMしました :envelope:')
  except Exception as e:
    respond(f':warning: エラーが起きました: {e}')
    return

def generate_dajare_select_block(dajare_texts: List[str]) -> dict:
  options = []
  for i, dajare_text in enumerate(dajare_texts):
    options.append({
      'text': {
        'type': 'plain_text',
        'text': f"No.{i}: {dajare_text}",
      },
      'value': dajare_text,
    })

  return {
    'type': 'section',
    'text': {
      'type': 'plain_text',
      'text': '生成された駄洒落を選択してください',
    },
    'accessory': {
      'type': 'static_select',
      'action_id': 'dajare_select',
      'placeholder': {
        'type': 'plain_text',
        'text': '駄洒落を選択してください',
      },
      'options': options,
    },
  }

@app.action('dajare_select')
def dajare_select_handler(ack, body, say, respond):
  ack()

  action = body['actions'][0]
  if action['type'] != 'static_select' or 'selected_option' not in action:
    respond(':warning: エラーが起きました')
    return

  selected_dajare_text = action['selected_option']['value']

  say(
    text=f"{selected_dajare_text}\nなーんちゃってwww",
    channel='#general'
  )

def get_dajare(text) -> List[str]:
  # 駄洒落APIを呼び出す
  request_url = 'https://dajare.herokuapp.com/api'
  response = requests.post(request_url, json={'text': text})

  if response.status_code != 200:
    raise response.raise_for_status()

  dajare_texts = response.json()['puns']
  if len(dajare_texts) == 0:
    raise Exception('No dajare found')

  # 駄洒落の重複を除去
  dajare_texts = list(set(dajare_texts))

  return dajare_texts

if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
