from fight_day.daily import Iciba

iciba = Iciba()
content = iciba.dailySentence.get('content')
note = iciba.dailySentence.get('note')
content_len = len(content) if len(content) > 40 else 40
print('*' * content_len)
print("这里是每日一句，祝您学习愉快！".center(content_len // 5 * 4))
print(content.center(content_len))
print(note.center(content_len // 5 * 4))
print('*' * content_len)
del content, note, content_len, iciba
