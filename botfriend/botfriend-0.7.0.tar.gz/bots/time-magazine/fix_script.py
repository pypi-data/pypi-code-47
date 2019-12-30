import datetime
import json
for i in open("script.json"):
    data = json.loads(i.strip())
    new_data = {}
    new_data['publish_at'] = data['post_date'] + ' 17:00'
    in_format = '%Y-%m-%d'
    content = datetime.datetime.strptime(data['date'], in_format).strftime("%B %d, %Y")
    new_data['content'] = content
    attachments = []
    new_data['attachments'] = attachments
    attachments.append(dict(path=data['path'], type='image/png'))
    print(json.dumps(new_data))
