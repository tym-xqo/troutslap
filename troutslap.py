from flask import Flask
from flask_slack import Slack
import requests
import json
import slack as slackapi
from slack import users
import os

app = Flask(__name__)
slack = Slack(app)
app.add_url_rule('/', view_func=slack.dispatch)

# On GCE, we have files mounted at /secret for
# incoming webhook URL and team token
# Or you can hard-code values in the except blocks below.
# try:
#     with open('/secret/hookurl', 'r') as hookf:
#         url = hookf.read().strip()
# except:
#     url = ("https://hooks.slack.com/services/"
#            "T02594HP0/B081REU01/PjOvu5UAGNgVKUTydc3GqS6L")  # <- fake ;)
# try:
#     with open('/secret/token', 'r') as tokenf:
#         valid = tokenf.read().strip()
# except:
#     valid = "bZKQqL4qkCOORlwzJRAPAvNc"  # phony
# try:
#     with open('/secret/teamid', 'r') as teamf:
#         team = teamf.read().strip()
# except:
#     team = "T02594HP0"  # phony
# try:
#     with open('/secret/slacktoken', 'r') as slacktokenf:
#         slacktoken = slacktokenf.read().strip()
# except:
#     slacktoken = "bZKQqL4qkCOORlwKQqzJRAPORlwzZKQqL4qkAvNc"

url = os.getenv('HOOKURL')
valid = os.getenv('TOKEN')
team = os.getenv('TEAM')
slacktoken = os.getenv('SLACKTOKEN')


@slack.command('slap', token=valid,
               team_id=team, methods=['POST'])
def slap_someone(**kwargs):
    channel = kwargs.get('channel_id')
    slappee = kwargs.get('text')
    payload = {'icon_emoji': ':fish:', 'username': 'Troutslap!',
               'channel': channel, 'unfurl_links': True}
    if slappee == '':
        message = '<http://i.imgur.com/R26mope.gifv>'
        payload.update({'text': message})
        r = requests.post(url, data=json.dumps(payload))
        return slack.response('')
    else:
        slappee = slappee.replace('@', '')
        slappee_id = user_id_from_name(slappee)

        slapper_id = kwargs.get('user_id')
        slapper = kwargs.get('user_name')

        message = ('<@{}|{}> slaps <@{}|{}> around a bit with a large trout!'
                   .format(slapper_id, slapper, slappee_id, slappee))
        payload.update({'text': message})
        r = requests.post(url, data=json.dumps(payload))
        return slack.response('')


def user_id_from_name(user):
    slackapi.api_token = slacktoken
    r = users.list()
    list = r['members']
    user_id = ''
    for u in list:
        if u['name'] == user:
            user_id = u['id']
    i = users.info(user_id)
    return i['user']['id']

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
