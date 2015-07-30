#Troutslap

- `/slap [@username]` to slap someone around a bit with a large trout!
- Or, `/slap` by itself to post a .gifv of the Python fish-slapping dance!

Run with Gunicorn, as shown in the Procfile. (TODO: add 'Deploy to Heroku' button)
Requires environment variables set for:

```
HOOKURL=[your Incoming Webhook link]
TOKEN=[Slash command token]
SLACKTOKEN=[Slack API token]
```

Slack API access needed to look up user_id for the Incoming Webhook payload.
