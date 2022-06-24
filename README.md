# Bolt Docker

A Docker container for receiving Slack Bolt Socket mode message events and sending to a webhook.

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
docker run --env-file .env bolt-docker
```
