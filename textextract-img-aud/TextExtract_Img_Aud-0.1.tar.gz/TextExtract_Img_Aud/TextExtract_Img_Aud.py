import os
import speech_recognition as sr
from pydub import AudioSegment
from bs4 import BeautifulSoup

import PIL.Image

import pytesseract

home = os.environ.get('Tesseract-OCR')
print (home)

r=sr.Recognizer()


def A2T(Ftype,path):
        form=Ftype
        print(form)
        if form== 'mp3':
            sound=AudioSegment.from_mp3(path)
            FinalOutput=sound.export(r"C:\Users\Dell\Downloads\outputmp3.wav", format="wav")
            audio=r'C:\Users\Dell\Downloads\outputmp3.wav'
            with sr.AudioFile(audio) as source:
                audio=r.record(source)
                text=r.recognize_google(audio)
                print(text)
                print("Take some time to create text file. So wait until the done message is displayed")
                output_file=open(r"C:\Users\Dell\Downloads\Audio_Text.txt","w+")
                output_file.write(text)
            print('done')
        elif form== 'aac':
            sound = AudioSegment.from_file(path)
            FinalOutput=sound.export(r"C:\Users\Dell\Downloads\outputaac.wav", format="wav")
            audio=r'C:\Users\Dell\Downloads\outputaac.wav'
            with sr.AudioFile(audio) as source:
                audio=r.record(source)
                text1=r.recognize_google(audio)
                print(text1)
                print("Take some time to create text file. So wait until the done message is displayed")
                output_file=open(r"C:\Users\Dell\Downloads\Audio_Text.txt","w")
                output_file.write(text1)
                print("Check Your Downlaod Folder for file name Audio_Text.txt ")
           
            print('done')
        elif form== 'wav':
            with sr.AudioFile(path) as source:
                audio=r.record(source)
                text2=r.recognize_google(audio)
                print(text2)
                print("Take some time to create text file. So wait until the done message is displayed")
                output_file=open(r"C:\Users\Dell\Downloads\Audio_Text.txt","w")
                output_file.write(text2)
                print("Check Your Downlaod Folder for file name Audio_Text.txt ")
           
            print('done')
        else:
            print("Enter Audio Format")
#A2T('mp3',r'C:\Users\Dell\Downloads\AudioFiles\Models_Etc.mp3')

def img2txt(path):
    img=PIL.Image.open(path)
    pytesseract.pytesseract.tesseract_cmd=(home)
    result=pytesseract.image_to_string(img)
    with open(r"C:\Users\Dell\Downloads\Image_To_Text.txt", "w") as text_file:
        text_file.write(result)
        ans=print("Check your download folder Image_To_Text.txt \n "+result)
    return(ans)
#img2txt(r'C:\Users\Dell\Downloads\Images\PythonKnowledgeGraph.png')
