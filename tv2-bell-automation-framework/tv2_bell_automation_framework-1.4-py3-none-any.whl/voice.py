import time
import speech_recognition as sr
from playsound import playsound


def play_audio(dut, audio_file, audio_command_text=None):
    try:
        playsound(audio_file)
        text_annotation_str = 'Playing the audio command'
        if audio_command_text:
            text_annotation_str += ' : %s' % audio_command_text
        dut.display.add_text_annotation(text_annotation_str, duration=5.0)
        dut.timestamps.append({'audio_cmd_play_time': time.time()})

    except Exception as e:
        print('EXCEPTION ARRIVED IN PLAY_SOUND :: ', e)

def speech_recognition(dut):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio_listen_start_time = time.time()
            dut.timestamps.append({'audio_listen_start_time': audio_listen_start_time})
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            # listens for the user's input
            audio = r.listen(source, timeout=15)
            if audio:
                dut.timestamps.append({'audio_listened_end_time': time.time()})
            text = r.recognize_google(audio)
            print("Text received: " + text)
            return text

        # Exception handler when google could not understand what was said
        except sr.UnknownValueError as e:
            print("Google Speech Recognition could not understand audio")
            return False

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return False

        except sr.WaitTimeoutError as e:
            dut.timestamps.append({'audio_listened_timeout_at': time.time()})
            audio_timeout_time_taken = time.time() - audio_listen_start_time
            dut.durations.append({'audio_timeout_time_taken': audio_timeout_time_taken})
            print('Listen Timeout at %s' % round(audio_timeout_time_taken, 2))
            return False
