# Dajare Slack App

This is a Slack App for Dajare (Japanese puns)!
You can get a random Dajare by using the command `/dajare`.

## Setup Slack App

Configure the Slack App settings like `manifest.json`.

## Development

> [!NOTE]
> - This document assumes that you have already created a Slack App and installed it to your workspace, and you have the tokens: `SLACK_BOT` and `SLACK_APP`.
>  If you don't have the tokens, you can get them from the Slack App settings and refer to the [official document](https://api.slack.com/quickstart).
> - This document assumes that your Slack App works in Socket Mode. If you don't enable Socket Mode, you can refer to the [official document](https://api.slack.com/apis/socket-mode).

### Requirements

- Python 3.6+
- Slack Workspace

### Setup

```bash
git clone https://github.com/satoryu/dajare-slack-app.git
cd dajare-slack-app
```

### Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
```

### Set up environment variables

If you don't have a Slack App, you can create it from [here](https://api.slack.com/apps).
This document assumes that you have already created a Slack App and installed it to your workspace, and you have the tokens: `SLACK_BOT` and `SLACK_APP`.

```bash
export SLACK_BOT_TOKEN=your_slack_bot_token
export SLACK_APP_TOKEN=your_slack_app_token
```

### Run the app

```bash
python app.py
```
