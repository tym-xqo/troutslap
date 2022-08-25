#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import slack
from dotenv import load_dotenv
from flask import Flask, request
from slack.errors import SlackApiError

app = Flask(__name__)

load_dotenv()

valid = os.getenv("TOKEN")
slacktoken = os.getenv("SLACKTOKEN")

client = slack.WebClient(slacktoken)


def slack_post(channel, blocks=[], title=None, message=None, color="#999999"):
    """Send a message to Slack"""
    attach = dict(fallback=message, title=title, text=message, color=color)
    try:
        post = client.chat_postMessage(
            channel=channel,
            attachments=[attach],
            username="Troutslap!",
            icon_emoji=":fish:",
            blocks=blocks,
        )
    except SlackApiError:
        # TODO: send something to poster here
        post = None
    return post


def slap_gif(channel):
    """Format a message that just sends a gif of the fish-slapping dance
    from Monty Python
    """
    blocks = [
        {
            "type": "image",
            "title": {"type": "plain_text", "text": "image1", "emoji": True},
            "image_url": "https://i.imgur.com/R26mope.gif",
            "alt_text": "image1",
        }
    ]
    response = slack_post(channel=channel, blocks=blocks)
    return response


@app.route("/", methods=["POST"])
def index():
    """Respond to Slack slash command.
    Generally expects a username, and sends a bot message like:
    `X slaps Y around a bit with a large trout!` where X is the sender
    and Y is a username specified in the text of the slash command request
    If the text is empty, it sends the fish-slapping dance gif
    """
    # Verify the token sent by the slash command
    if request.form["token"] != valid:
        return "nope", 403

    # TODO: figure out DMs
    channel = request.form["channel_id"]

    if request.form["text"] == "":
        slap_gif(channel)

    else:
        slapped_user = request.form["text"]

        slapping_user_id = request.form["user_id"]
        slapping_user = request.form["user_name"]

        message = "<@{}|{}> slaps {} around a bit with a large trout!".format(
            slapping_user_id, slapping_user, slapped_user
        )
        slack_post(channel=channel, message=message)
    return "", 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
