from typing import  NamedTuple
from datetime import datetime

import subprocess
import os.path


class MGAudio(NamedTuple):
    path: str
    delay: float


class MGVideo(NamedTuple):
    path: str


class MergeAudioVideo:

    video_file = None
    audio_files = None
    output_file_name = None

    def __init__(self, video_file: MGVideo, audio_files:[MGAudio], output_file_name:str=None):
        self.video_file = video_file
        self.audio_files = audio_files
        self.output_file_name = output_file_name

        if self.audio_files is None:
            raise Exception("At least one audio file expected.")
        elif len(self.audio_files) <= 0:
            raise Exception("At least one audio file expected.")

    # def merge(self):
    #     video_w_audio_channel = self.add_audio_channel()
    #
    #     if video_w_audio_channel is not None:
    #         lst_merge_audio = []
    #         lst_mix_audio = []
    #         audio_files_len = len(self.audio_files)
    #         lst_command = ["ffmpeg", "-y", "-i", video_w_audio_channel]
    #
    #         for i in range(audio_files_len):
    #             str_index = (i + 1)
    #             audio = self.audio_files[i]
    #             lst_command.extend(["-i", audio.path])
    #             str_audio = '[%s]adelay=%s|%s[S%s]' % (str_index, (audio.delay * 1000), (audio.delay * 1000), str_index)
    #             lst_merge_audio.append(str_audio)
    #             lst_mix_audio.append("[S" + str(str_index) + "]")
    #
    #         self.output_file_name = self.output_file_name if self.output_file_name is not None else ("output_file_%s.mp4" % int(datetime.timestamp(datetime.now())))
    #
    #         print("MERGED VIDEO FILE NAME:- ", self.output_file_name)
    #
    #         filter_complex = "%s;[0]%samix=%s[mixout]" % (";".join(lst_merge_audio),"".join(lst_mix_audio), (audio_files_len + 1))
    #         lst_command.extend(["-filter_complex", filter_complex, "-map", "0:v", "-map", "[mixout]", "-c:v", "copy" , self.output_file_name])
    #
    #         #print(lst_command)
    #
    #         try:
    #             process = subprocess.Popen(lst_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #             output, err = process.communicate()
    #             print(err)
    #             os.remove("test.txt")
    #             return True, None
    #         except Exception as exp:
    #             return False, exp

    def merge(self):
        video_w_audio_channel = self.add_audio_channel()

        if video_w_audio_channel is not None:
            lst_audio_input = []
            lst_merge_audio = []
            lst_mix_audio = []
            audio_files_len = len(self.audio_files)

            for i in range(audio_files_len):
                str_index = (i + 1)
                audio = self.audio_files[i]
                str_audio = '[%s]adelay=%s|%s[S%s]' % (str_index, (audio.delay * 1000), (audio.delay * 1000), str_index)
                lst_audio_input.append("-i " + audio.path)
                lst_merge_audio.append(str_audio)
                lst_mix_audio.append("[S" + str(str_index) + "]")

            self.output_file_name = self.output_file_name if self.output_file_name is not None else ("output_file_%s.mp4" % int(datetime.timestamp(datetime.now())))
            audio_input = " ".join(lst_audio_input)
            filter_complex = "%s;[0]%samix=%s[mixout]" % (";".join(lst_merge_audio),"".join(lst_mix_audio), (audio_files_len + 1))
            final_command = "ffmpeg -i %s %s -filter_complex \"%s\" -map 0:v -map [mixout] -c:v copy %s" % (video_w_audio_channel, audio_input, filter_complex, self.output_file_name)

            print(final_command)
            print('NEW FILE NAME : ', self.output_file_name)

            try:
                os.system(final_command)
                os.remove(video_w_audio_channel)
                return True, self.output_file_name
            except Exception as exp:
                return False, exp

    def add_audio_channel(self):
        print('IN AUDIO')
        out_file_w_audio = ("out_file_w_%s.mp4" % int(datetime.timestamp(datetime.now())))
        #lst_command = ["ffmpeg", "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100", "-i", self.video_file.path, "-shortest", "-c:v", "copy", "-c:a", "aac", out_file_w_audio]
        #print(lst_command)
        #process = subprocess.Popen(lst_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #output, err = process.communicate()
        #print(err)

        command = "ffmpeg -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 -i %s -shortest -c:v copy -c:a aac %s" % (self.video_file.path, out_file_w_audio)
        print("Command:- ", command)
        try:
            os.system(command)
        except Exception as e:
            print('Exception :: ', e)

        if os.path.exists(out_file_w_audio):
            print("In the if condition")
            return out_file_w_audio

        print("Out of condition")

        return None