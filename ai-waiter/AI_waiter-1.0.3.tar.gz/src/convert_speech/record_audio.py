# Import the necessary modules.
import tkinter
import tkinter as tk
import tkinter.messagebox
import pyaudio
import wave
import os
import sys
sys.path.append('../../')
from datetime import datetime
import keyboard

class RecAUD_space:
    """
    Record audio interface.
    Options to start, stop and cancel recording
    It saves to file automatically when you stop recording.

    Operates by using the keyboard as opposed to pressing buttons
    """

    def __init__(self, file_name, chunk=3024, frmat=pyaudio.paInt16, channels=2, rate=44100, py=pyaudio.PyAudio()):

        # Start Tkinter and set Title

        # set to hit space to record and stop record
        # esc to cancel?
        # output table number, order, time ordered

        # slide on what it's doing with confidence scores etc.

        self.main = tkinter.Tk()
        self.collections = []
        self.main.geometry('300x150') # size of buttons
        self.main.title('Record') # title of interface
        self.CHUNK = chunk
        self.FORMAT = frmat
        self.CHANNELS = channels
        self.RATE = rate
        self.p = py
        self.frames = []
        self.st = 1 # start counter
        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        current_time = str(datetime.now())
        current_time = "_".join(current_time.split()).replace(":","-")
        self.current_time = current_time[:-7]
        self.file_name = file_name

        self.labelframe = tkinter.LabelFrame(self.main, text = "Could I take your order?")
        self.labelframe.unbind("<space>")
        self.labelframe.bind("<space>", self.start_record)
        
        #self.labelframe.bind("<space>", self.stop)
        self.labelframe.bind("<Escape>", self.cancel_record)
        self.labelframe.pack(fill=tk.BOTH, expand = "yes")
        self.label = tkinter.Label(self.labelframe
        , text = "Press space bar to record, and again to stop.\n Press ESC to cancel.")
        self.label.pack()
        self.labelframe.focus_set()
        
        # Set Frames
        self.labelframe.mainloop()

    def start_record(self, event):
        """
        Start recording audio command
        """
        self.st = 1
        self.frames = []
        stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        #print("recording your order")
        while self.st == 1:
            data = stream.read(self.CHUNK)
            print("recording your order")
            self.frames.append(data)
            self.main.update()
            if keyboard.is_pressed('space'):
                #self.labelframe.unbind("<space>")
                self.st = 0
                stream.close()

                wf = wave.open(self.file_name, 'wb')
                wf.setnchannels(self.CHANNELS)
                wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
                wf.setframerate(self.RATE)
                wf.writeframes(b''.join(self.frames))
                wf.close()
                print('Written to file' , self.file_name, 'at time:' + self.current_time)
                self.main.destroy()

        # stream.close()

        # wf = wave.open(self.file_name, 'wb')
        # wf.setnchannels(self.CHANNELS)
        # wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        # wf.setframerate(self.RATE)
        # wf.writeframes(b''.join(self.frames))
        # wf.close()
        # print('Written to file' , self.file_name, 'at time:' + self.current_time)
        # self.main.destroy()
        return None        
    
    def stop(self, event):
        """
        Stop recording audio command
        sets counter to 0
        """
        self.st = 0
        return None 

    def cancel_record(self, event):
        """
        Cancels recording without saving
        Stops execution
        """
        sys.exit("Cancelled Recording")
        return None
    


class RecAUD:
    """
    Record audio interface.
    Options to start, stop and cancel recording
    It saves to file automatically when you stop recording.
    """

    def __init__(self, file_name, chunk=3024, frmat=pyaudio.paInt16, channels=2, rate=44100, py=pyaudio.PyAudio()):

        # Start Tkinter and set Title

        # set to hit space to record and stop record
        # esc to cancel?
        # output table number, order, time ordered

        # slide on what it's doing with confidence scores etc.

        # set to black
        # output time
        # save to csv

        self.main = tkinter.Tk()
        self.collections = []
        self.main.geometry('300x150') # size of buttons
        self.main.title('Record') # title of interface
        self.CHUNK = chunk
        self.FORMAT = frmat
        self.CHANNELS = channels
        self.RATE = rate
        self.p = py
        self.frames = []
        self.st = 1 # start counter
        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        current_time = str(datetime.now())
        current_time = "_".join(current_time.split()).replace(":","-")
        self.current_time = current_time[:-7]
        self.file_name = file_name

        # Set Frames
        self.buttons = tkinter.Frame(self.main, padx=20, pady=20)

        # Pack Frame
        self.buttons.pack(fill=tk.BOTH)

        # Start, Stop and Cancel buttons
        self.strt_rec = tkinter.Button(self.buttons, width=10, padx=10, pady=5,
         text='Start Recording', command=lambda: self.start_record())
        
        self.strt_rec.grid(row=0, column=0, padx=5, pady=5)
        self.stop_rec = tkinter.Button(self.buttons, width=10, padx=10, pady=5,
         text='Stop Recording', command=lambda: self.stop())
        self.stop_rec.grid(row=0, column=1, columnspan=1, padx=5, pady=5)
        self.cancel_rec = tkinter.Button(self.buttons, width=20, padx=0, pady=5,
         text='Cancel', command=lambda: self.cancel_record())
        self.cancel_rec.grid(row=1, column=0, columnspan=2, padx=50, pady=5)

        tkinter.mainloop()

    def start_record(self):
        """
        Start recording audio command
        """
        self.st = 1
        self.frames = []
        stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        while self.st == 1:
            data = stream.read(self.CHUNK)
            self.frames.append(data)
            print("* recording")
            self.main.update()

        stream.close()

        wf = wave.open(self.file_name, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        print('Written to file' , self.file_name, 'at time:' + self.current_time)
        self.main.destroy()
        return None        
    
    def stop(self):
        """
        Stop recording audio command
        sets counter to 0
        """
        self.st = 0
        return None 

    def cancel_record(self):
        """
        Cancels recording without saving
        Stops execution
        """
        sys.exit("Cancelled Recording")
        return None




if __name__ == "__main__":
    # Create an object of the ProgramGUI class to begin the program.
    guiAUD = RecAUD_space('audio.wav')