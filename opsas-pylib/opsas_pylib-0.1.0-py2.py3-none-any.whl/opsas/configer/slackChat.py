import datetime

import requests


def current_time():
    return datetime.datetime.now().strftime("%F %H:%M:%S")


if __name__ == '__main__':
    api = "https://slack.com/api/chat.postMessage"
    token = "xoxp-867152376579-867152377235-878699231648-e6de39548da2b289efbfde6ad2458a3d"
    jenkins_bot_token = "xoxb-867152376579-891937470980-hkSS1FJLindmtvV3jx3YFFyt"

    s = requests.session()
    s.headers.setdefault('Authorization', 'Bearer ' + token)
    s.headers.setdefault('Content-type', 'application/json')
    payload = {
        'channel': "opsas",
        'blocks': [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Start Thread *<https://www.baidu.com|ConsoleLog>*"
                }
            }
        ]
    }

    conn = s.post(api, json=payload)
    res = conn.json()
    print(res)
    parrent_ts = res['ts']
    conn = s.post(api, json=dict(
        channel='opsas',
        thread_ts=parrent_ts,
        reply_broadcast=False,
        blocks=[
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "http://img.justcalm.ink/warn.png",
                        "alt_text": "warning icon"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"{current_time()}"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Conflicts with Team Huddle: 4:15-4:30pm*"
                }
            }
        ],
        as_user=True
    ))
    print(conn.json())
