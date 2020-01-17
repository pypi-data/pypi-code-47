
import sys
sys.path.append('../')
#from src.convert_speech.record_audio import RecAUD, RecAUD_space
import src.convert_speech.record_audio2 as record_audio
from src.convert_speech.speech_to_text import SpeechConvert
from src.configs.config import filenames
import src.convert_text.get_menu_items as get_menu
import src.convert_text.text_to_command as get_command
import speech_recognition as sr
import src.gui.display_window2 as display_qt
from PySide2 import QtWidgets as qtw
import qdarkstyle
import os
os.chdir('..')


#import text_to_command
def main(audio_file, menu_file, final_orders):

    app = qtw.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    w1, timestamp =record_audio.main()
    print(timestamp)
    w1.show()
    app.exec_()
    w1.closed

    #RecAUD(audio_file)
    r = sr.Recognizer()
    audio = SpeechConvert(audio_file, r)
    menu = get_menu.main(menu_file)
    get_command.main(audio, timestamp, r, menu)

    #sys.exit(app.exec_())

if __name__ == "__main__":
    audio_file = filenames.audio_file2
    #r = sr.Recognizer()
    #audio = SpeechConvert(audio_file, r)
    menu_file = filenames.menu_file
    gui_photo = filenames.gui_photo
    final_orders = filenames.final_orders
    main(audio_file, menu_file, final_orders)
