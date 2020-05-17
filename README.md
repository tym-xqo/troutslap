# Troutslap

A Slack slash command responder for people who remember mIRC!

- `/slap [@username]` to slap someone around a bit with a large trout!
- Or, `/slap` by itself to post a .gif of the fish-slapping dance from Monty Python!

Run with Gunicorn, as shown in the Dockerfile.
Requires environment variables set for:

```sh
TOKEN=<Slash command token>
SLACKTOKEN=<Slack API token>
```

The `text` field of the slash command request is used to say who gets slapped. This mostly just gets passed through unaltered, but if you want the slapped user to get notified as a mention, just be sure to check the 'Escape channels, users, and links sent to your app' option when setting up the command the Slack app admin UI.
