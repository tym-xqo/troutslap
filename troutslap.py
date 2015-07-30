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

url = os.getenv('HOOKURL')
slacktoken = os.getenv('SLACKTOKEN')


@slack.command('slap', token=os.getenv('TOKEN'),
               team_id=os.getenv('TEAM'), methods=['POST'])
def slap_someone(**kwargs):
    channel = kwargs.get('channel_name')
    channel = u'#%s' % channel
    slappee = kwargs.get('text')
    if slappee == '':
        message = '<http://i.imgur.com/R26mope.gifv>'
        payload = {'text': message, 'unfurl_links': True, 'icon_emoji': ':fish:',
        'username': 'Troutslap!', 'channel': channel}
        r = requests.post(url, data=json.dumps(payload))
        return slack.response('')
    else:
        slappee = slappee.replace('@','')
        slappee_id = user_id_from_name(slappee)

        slapper_id = kwargs.get('user_id')
        slapper = kwargs.get('user_name')

        message = '<@%s|%s> slaps <@%s|%s> around a bit with a large trout!' % (
           slapper_id, slapper, slappee_id, slappee)

        payload = {'text': message, 'icon_emoji': ':fish:',
        'username': 'Troutslap!', 'channel': channel}
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

