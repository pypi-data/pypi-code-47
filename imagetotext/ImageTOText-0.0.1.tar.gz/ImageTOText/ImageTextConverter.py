import os
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import numpy as np
import csv
import cv2
import PIL.Image
import PIL.Image, PIL.ImageTk

import PIL.Image
import cv2
import PyPDF2
import PIL.Image
import PIL.Image, PIL.ImageTk
from PIL import ImageTk,Image

import re
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import pytesseract
#import imgxt as x
import requests
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame
import os
#import magic
import urllib.request

import os

import requests
from bs4 import BeautifulSoup
import numpy as np
import csv
import cv2
import PIL.Image
import PIL.Image, PIL.ImageTk



def img2txt(path):
    img=PIL.Image.open(path)
    pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    result=pytesseract.image_to_string(img)
    with open(r"C:\Users\Dell\Downloads\Image_To_Text.txt", "w") as text_file:
        text_file.write(result)
        ans=print("Check your download folder Image_To_Text.txt \n "+result)
    return(ans)

                        #flash('File successfully uploaded')
                        #flash('Check your download folder Image_To_Text.txt')


