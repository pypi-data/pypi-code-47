import argparse
from gtts import gTTS

# Text command to convert into audio file
text_command = 'OK Google, open settings on the Living Room TV'

parser = argparse.ArgumentParser()
parser.add_argument('--text', default=text_command,
                    help='Actual text command to convert to audio file (mp3)')
args = parser.parse_args()


def text_to_speech(text_command=args.text):
    tts = gTTS(text=text_command, lang='en')
    tts.save('text_command_audio.mp3')


if __name__ == '__main__':
    text_to_speech()
