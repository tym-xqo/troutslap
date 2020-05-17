# Troutslap

A Slack slash command responder for people who remember mIRC!

- `/slap [@username]` to slap someone around a bit with a large trout!
- Or, `/slap` by itself to post a .gif of the fish-slapping dance from Monty Python!

Run with Gunicorn, as shown in the Dockerfile.
Requires environment variables set for:

```sh
TOKEN=[Slash command token]
SLACKTOKEN=[Slack API token]
```

Slack API access needed to look up user_id for the post payload.
