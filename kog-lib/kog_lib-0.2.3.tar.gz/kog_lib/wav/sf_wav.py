import os,struct,math

class SFWav:
    def __init__(self,wav_path=None):
        self.wav_path = ""
        self.wav_head = ""
        if wav_path:
            self.open(wav_path)

    @staticmethod
    def help():
        print("""
        ----------------------SFWav类 使用方法--------------------------------------
        import kog_lib\n
        实例化：
            my_wav = kog_lib.SFWav(wav_path)
            或，
            my_wav = kog_lib.SFWav()
            my_wav.open(wav_path)\n
        获取主要参数：(声道数、样本宽度、采样率、总帧数)
            my_wav.getparams()\n
        得到区间内峰值：
            my_wav.get_peak(selected_channel,start_time,end_time)
                selected_channel: 要得到哪个声道的数据，默认1声道
                start_time: 起始时间，默认0
                end_time: 终止时间，默认总时长\n
        切割音频: 从start_time开始且切到end_time时长的音频，保存到output
            my_wav.cut_wav(output,start_time,end_time,selectedchannel=1)
                默认切取第一个声道的信息，保存为单声道音频\n
        其他方法：
            my_wav.readframes(nframes,start_frame) # 从第几帧开始读取多少帧
            my_wav.readframes_bytime(start_time,end_time) # 从第几秒开始读到第几秒
        ----------------------------------------------------------------------------
        """)

    def open(self,wav_path):
        self.wav_path = wav_path
        self.wav_head = self.get_wav_head(self.wav_path)
        self.__validate_dataset()

    def getparams(self):
        return self.wav_head.getparams()

    def readframes(self,nframes,start_frame):
        framewidth = self.wav_head.get_framewidth()
        start_pos = self.__get_pos_byframe(start_frame)
        bytesize = nframes*framewidth
        file_handler = SFWavFileHandler()
        return file_handler.read_file(self.wav_path,start_pos,bytesize)

    def readframes_bytime(self,start_time,end_time=0):
        if end_time == 0:
            end_time = self.wav_head.get_duration()
        self.__validate_get_peak_params(1,start_time,end_time)
        start_frame = self.__get_frame_bytime(start_time)
        end_frame = self.__get_frame_bytime(end_time)
        nframes = end_frame - start_frame
        return self.readframes(nframes,start_frame)

    def get_samples_bytime(self,start_time,end_time):
        raw_data = self.readframes_bytime(start_time,end_time)
        return self.__parse_samples(raw_data)

    def get_samples_bychannel(self,samples,selectedchannel):
        samples_size = len(samples)
        nchannels = self.wav_head.get_nchannels()
        nframes = round(samples_size/nchannels)
        selected_channel_samples = []
        if selectedchannel > nchannels or selectedchannel < 1:
            raise ValueError(f"没有这个声道，selectedchannel={selectedchannel}")
        for ind in range(nframes):
            pos = (selectedchannel-1) + ind*nchannels
            selected_channel_samples.append(samples[pos])
        return selected_channel_samples

    def get_peak(self,selectedchannel=1,start_time=0,end_time=0):
        if end_time == 0:
            end_time = self.wav_head.get_duration()
        self.__validate_get_peak_params(selectedchannel,start_time,end_time)
        samples = self.get_samples_bytime(start_time,end_time)
        selected_channel_samples = self.get_samples_bychannel(samples,selectedchannel)
        max_value = max(selected_channel_samples)
        min_value = min(selected_channel_samples)
        cut_duration = end_time-start_time
        return max_value,min_value,cut_duration

    def cut_wav(self,file_path,start_time,end_time=0,selectedchannel=1):
        if end_time == 0:
            end_time = self.wav_head.get_duration()
        self.__validate_get_peak_params(selectedchannel,start_time,end_time)
        samples = self.get_samples_bytime(start_time,end_time)
        selected_channel_samples = self.get_samples_bychannel(samples,selectedchannel)
        print(start_time,end_time,len(selected_channel_samples))
        self.__write_wav_file(file_path,selected_channel_samples,\
                              self.wav_head.get_samplewidth(),\
                              self.wav_head.get_framerate())

    def __validate_get_peak_params(self,selectedchannel,start_time,end_time):
        total_duration = self.wav_head.get_duration()
        if start_time < 0 or selectedchannel < 0 or end_time < 0:
            raise ValueError(f"参数错误，有参数小于0，{start_time}{end_time}{selectedchannel}")
        if start_time > end_time:
            raise ValueError(f"参数错误，起始时间{start_time}大于终止时间{end_time}")
        if end_time > total_duration:
            raise ValueError(f"参数错误，终止时间{end_time}大于总时长{total_duration}")
        if selectedchannel > self.wav_head.get_nchannels():
            raise ValueError(f"参数错误，没有这个声道{selectedchannel},总声道数{self.wav_head.get_nchannels()}")

    def __write_wav_file(self,file_path,dataset,samplewidth,frame_rate,nchannels=1):
        nframes = len(dataset)
        dataset_size = nframes * samplewidth * nchannels
        chunck_size = dataset_size + 36
        fmt_size = 16
        audio_fmt = 1        
        byte_rate = frame_rate * samplewidth
        block_align = nchannels * samplewidth
        bitspersample = 8 * samplewidth
        try:
            unpack_filter = self.__get_unpack_filter(samplewidth)
            wav_head_data = (b'RIFF',chunck_size,b'WAVE',b'fmt ',fmt_size,\
                        audio_fmt,nchannels,frame_rate,byte_rate,\
                        block_align,bitspersample,b'data',dataset_size)
            wav_head_fmt = "<4sI4s4sIHHLLHH4sI"
            wav_dataset_fmt = str(nframes)+unpack_filter
            packed_wav_head = struct.pack(wav_head_fmt,*wav_head_data)
            packed_wav_dataset = struct.pack(wav_dataset_fmt,*dataset)
        except Exception as e:
            raise ValueError(f"wav数据打包错误，{e}")

        try:
            packed_wav_data = packed_wav_head + packed_wav_dataset
            with open(file_path,'wb') as fb:
                fb.write(packed_wav_data)
        except Exception as e:
            raise IOError(f"wav数据写入{file_path}出错，{e}")


    
    def __parse_samples(self,rawdata):
        samplewidth = self.wav_head.get_samplewidth()
        unpack_filter = self.__get_unpack_filter(samplewidth)
        unpack_filter = str(int(len(rawdata)/samplewidth))+unpack_filter
        if unpack_filter == "":
            raise ValueError(f"没有找到相应(samplewidth:{samplewidth})的解码参数")
        return struct.unpack(unpack_filter,rawdata)

    def __get_unpack_filter(self,samplewidth):
        if samplewidth == 1:
            return 'B'
        if samplewidth == 2:
            return 'h'
        if samplewidth == 4:
            return 'f'
        return ''

    def __get_frame_bytime(self,time):
        framerate = self.wav_head.get_framerate()
        return int(round(time*framerate))

    def __get_pos_byframe(self,framecount):
        dataset_startpos = self.wav_head.get_dataset_startpos()
        framewidth = self.wav_head.get_framewidth()
        return dataset_startpos + framecount * framewidth

    def get_wav_head(self,file_path):
        return SFWavHeader(file_path)

    def __validate_dataset(self):
        samplewidth = self.wav_head.get_samplewidth()
        datasize = self.wav_head.get_dataset_size()
        framewidth = self.wav_head.get_framewidth()
        if self.__get_unpack_filter(samplewidth) == "":
            raise TypeError(f"{self.wav_path}不属于 8 16 32bit音频的任意一种")
        if datasize % framewidth != 0:
            raise ValueError(f"{self.wav_path}的数据块大小有误")


class SFWavHeader:

    def __init__(self,wav_path=None):
        self.wav_path = ""
        self.raw_data = ""
        if wav_path:
            self.open(wav_path)

    def getparams(self):
        nchannels = self.get_nchannels()
        samplewidth = self.get_samplewidth()
        framerate = self.get_framerate()
        nframes = self.get_nframes()
        return nchannels,samplewidth,framerate,nframes

    def get_nchannels(self):
        return self.unpack_dict['channels']

    def get_samplewidth(self):
        return int(self.unpack_dict['bits']/8)

    def get_framerate(self):
        return self.unpack_dict['samplerate']

    def get_framewidth(self):
        samplewidth = self.get_samplewidth()
        nchannels = self.get_nchannels()
        return samplewidth*nchannels

    def get_nframes(self):
        framewidth = self.get_framewidth()
        return int(self.unpack_dict['datasize']/framewidth)

    def get_duration(self):
        nframes = self.get_nframes()
        framerate = self.get_framerate()
        return nframes/framerate

    def get_dataset_startpos(self):
        return self.unpack_dict['dataset_startpos']

    def get_dataset_size(self):
        return self.unpack_dict['datasize']

    def get_head_head(self):
        return self.head_head

    def open(self,wav_path):
        self.wav_path = wav_path
        file_handler = SFWavFileHandler()
        self.raw_data = file_handler.read_file(wav_path,0,1000)
        self._validate_rawdata()
        self.__parse_params()

    def print_head(self):
            print("\n声道数："+str(self.get_nchannels()))
            print("样本宽度："+str(self.get_samplewidth()))
            print("采样率："+str(self.get_framerate()))
            print("帧数："+str(self.get_nframes()))
            print("总时长："+str(self.get_duration()))
            print("数据集起始点："+str(self.get_dataset_startpos()))
            print("数据集大小："+str(self.get_dataset_size())+"\n")

    def __parse_params(self):
        self.unpack_dict = {}
        self.unpack_dict['wav_path'] = self.wav_path
        data_set_startpos = self._get_data_set_startpos()
        self.unpack_dict['dataset_startpos'] = data_set_startpos
        (self.unpack_dict['datasize'],) = struct.unpack("<L",self.raw_data[data_set_startpos-4:data_set_startpos])

        self.unpack_dict['pcmtype'], \
        self.unpack_dict['channels'], \
        self.unpack_dict['samplerate'], \
        self.unpack_dict['bytespersec'], \
        self.unpack_dict['alignment'], \
        self.unpack_dict['bits'] = struct.unpack("<HHLLHH",self.raw_data[20:36])
        self.head_head = {}
        self.head_head['RIFF'],\
        self.head_head['chunksize'],\
        self.head_head['WAVE'],\
        self.head_head['fmt '],\
        self.head_head['fmtsize'] = struct.unpack("<4sI4s4sI",self.raw_data[:20])

    def _validate_rawdata(self):
        if self.raw_data == "":
            raise ValueError(f"{self.wav_path} 没有读取到内容")
        if self.raw_data[0:4] != b"RIFF":
            raise TypeError(f"{self.wav_path} 不是标准的RIFF:{self.raw_data[0:4]}")

    def _get_data_set_startpos(self):
        for ind,char in enumerate(self.raw_data):
            if self.raw_data[ind:ind+4] == b"data":
                return ind+8
        raise ValueError(f"{self.wav_path} 头部中没有data标识，文件内容有误")


class SFWavFileHandler:
    def read_file(self,file_path,start_pos,data_size,end_pos=0):
        if not os.path.isfile(file_path):
            raise FileExistsError(f"{file_path}不存在")
        size,end = self.__parse_params(file_path,start_pos,data_size,end_pos)
        self.__validate_params(start_pos,size,end)
        return self.__read_by_size(file_path,start_pos,size)

    @staticmethod
    def __read_by_size(file_path,start_pos,data_size):
        try:
            fp = open(file_path,"rb")
            fp.seek(start_pos)
            data = fp.read(data_size)
        except Exception as e:
            data = ""
            raise IOError(f"{file_path}: {e}")
        finally:
            fp.close()
            return data

    def __validate_params(self,start_pos,data_size,end_pos):
        if type(start_pos) is not int \
            or type(data_size) is not int \
            or type(end_pos) is not int:
            raise ValueError(f"参数必须是整数:(start_pos,{start_pos})(data_size,{data_size})(end_pos,{end_pos})")
        if start_pos > end_pos:
            raise ValueError(f"起始位置{start_pos}大于终止位置{end_pos}")
        if (end_pos - start_pos) < data_size:
            raise ValueError(f"读取范围小于所需数据大小:{end_pos-start_pos}<{data_size}")


    def __parse_params(self,file_path,start_pos,data_size,end_pos):
        if end_pos == 0:
            end_pos = os.path.getsize(file_path)
        if data_size == 0:
            data_size = end_pos - start_pos
        return data_size,end_pos
