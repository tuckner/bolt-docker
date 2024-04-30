# Bolt Docker

A Docker container for receiving Slack Bolt [Socket](https://api.slack.com/apis/connections/socket) mode message events and sending to a webhook. Helpful in environments that support webhooks and not websockets, but the webhooks are not internet facing.

## Setup Environment

Create a `.env` file with the following variables:

```
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-1-...
WEBHOOK_ADDRESS=https://...
```

## Build

```
docker build . -t bolt-docker
```

## Run

```
docker run -it -d --env-file .env --name slack-messages bolt-docker
```
