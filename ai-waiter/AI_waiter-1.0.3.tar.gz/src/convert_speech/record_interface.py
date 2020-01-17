""" 
test space bar to record audio
"""

import tkinter
import keyboard
import sys
import pyaudio

# def greet(event):
#     print('hello')

# def farewell(event):
#     print('bye')

# root = tkinter.Tk()
# frame = tkinter.Frame(root, width = 100, height = 100)
# frame.bind("<space>", greet)
# frame.bind("<Return>", farewell)
# frame.pack()
# frame.focus_set()
# frame.mainloop()

def start(event):
    """
    Start recording audio command
    """
    st = 1
    #stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    while st == 1:
        print("hello")
        if keyboard.is_pressed('space'):
            st = 0
            sys.exit("Stopped")



def cancel(event):
    sys.exit("Cancelled recording")

def record(file_name, chunk=3024, frmat=pyaudio.paInt16, channels=2, rate=44100, py=pyaudio.PyAudio()):


    main = tkinter.Tk()

    labelframe = tkinter.LabelFrame(main, text = "Could I take your order?")
    labelframe.pack(fill=tkinter.BOTH, expand = "yes")
    labelframe.bind("<space>", start)
    labelframe.bind("<Escape>", cancel)
    label = tkinter.Label(labelframe
    , text = "Press space bar to record, and again to stop.\n Press ESC to cancel.")
    label.pack()
    labelframe.focus_set()
    labelframe.mainloop()
    
record("hello")