import qdarkstyle
import sys
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc
from PySide2 import QtMultimedia as qtmm

sys.path.append('../../')
from src.configs.config import filenames
from datetime import datetime
import time

audiofile2 = filenames.audio_file2

class MainWindow(qtw.QMainWindow):
    closed = qtc.Signal()

    def __init__(self):
        """
        MainWindow constructor:
        Code in this method should define window properties, create backend resources, etc.
        """
        super().__init__()
        self.setWindowTitle("Record Order")

        #Create Window layout with a sound widget
        soundboard = qtw.QWidget()
        soundboard.setLayout(qtw.QGridLayout())
        self.setCentralWidget(soundboard)
        sw = SoundWidget()
        soundboard.layout().addWidget(sw)

        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("AI Waiter")

        #Window Dimensions
        self.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.MinimumExpanding)

        # Code ends here
        #self.show()

        # @qtc.Slot()
        # def exit_app(self, checked):
        #     sys.exit()

        sw.sendorder_button.clicked.connect(self.close)

    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)

class PlayButton(qtw.QPushButton):
    play_stylesheet = 'color: white;'
    stop_stylesheet = 'background-color: darkred; color: white;'

    def __init__(self):
        super().__init__('Play')
        self.setStyleSheet(self.play_stylesheet)

    def on_state_changed(self, state):
        if state == qtmm.QMediaPlayer.PlayingState:
            self.setStyleSheet(self.stop_stylesheet)
            self.setText('Stop')
        else:
            self.setStyleSheet(self.play_stylesheet)
            self.setText('Play')


class RecordButton(qtw.QPushButton):
    record_stylesheet = 'background-color: green; color: white;'
    stop_stylesheet = 'background-color: darkred; color: white;'

    def __init__(self):
        super().__init__('Record')
        self.setFont(qtg.QFont('Sans', 14, qtg.QFont.Bold))
        self.setStyleSheet(self.record_stylesheet)
        self.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)

    def on_state_changed(self, state):
        if state == qtmm.QAudioRecorder.RecordingState:
            self.setStyleSheet(self.stop_stylesheet)
            self.setText('Stop')
        else:
            self.setStyleSheet(self.record_stylesheet)
            self.setText('Record')

class SendOrderButton(qtw.QPushButton):
    button_stylesheet = 'background-color: blue; color: white;'

    def __init__(self):
        super().__init__('Send Order')
        self.setFont(qtg.QFont('Sans', 14, qtg.QFont.Bold))
        self.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        self.setStyleSheet(self.button_stylesheet)
        #self.clicked.connect(self.close)

    def press_button(self):
        if self.isEnabled():
            self.setEnabled(False)
            self.setText('Send Order')
        else:
            self.setEnabled(True)
            self.setText('Sent')

class SoundWidget(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QGridLayout())

        # Title
        self.label = qtw.QLabel("May I take your order?")
        self.label.setFont(qtg.QFont('Sans', 18, qtg.QFont.Bold))
        self.layout().addWidget(self.label, 0, 0, 1, 2)

        # Playback Subtitle
        self.label = qtw.QLabel("No Recording yet")
        self.layout().addWidget(self.label, 1, 0, 1, 2)

        #Play Button
        self.play_button = PlayButton()
        self.layout().addWidget(self.play_button, 3, 1, 1, 1)

        self.player = qtmm.QMediaPlayer()
        self.play_button.clicked.connect(self.on_playbutton)
        self.player.stateChanged.connect(self.play_button.on_state_changed)

        # Loading files Button
        self.file_button = qtw.QPushButton('Load File', clicked=self.get_file)
        self.layout().addWidget(self.file_button, 3, 0, 1, 1)

        # Slider
        self.position = qtw.QSlider(minimum=0, orientation=qtc.Qt.Horizontal)
        self.layout().addWidget(self.position, 2, 0, 1, 2)

        self.player.positionChanged.connect(self.position.setSliderPosition)
        self.player.durationChanged.connect(self.position.setMaximum)
        self.position.sliderMoved.connect(self.player.setPosition)

        # Volume
        # self.volume = qtw.QSlider(minimum=0,maximum=100,sliderPosition=10,
        #     orientation=qtc.Qt.Horizontal,
        #     #sliderMoved=self.player.setVolume
        # )
        # self.layout().addWidget(self.volume, 2, 0)

        # Recording
        self.recorder = qtmm.QAudioRecorder()

        # supported audio inputs
        print(self.recorder.audioInputs())
        self.recorder.setAudioInput('default:')

        #Overriding sound recording settings
        settings = qtmm.QAudioEncoderSettings()
        settings.setCodec('audio/pcm')
        settings.setSampleRate(44100)
        settings.setQuality(qtmm.QMultimedia.HighQuality)
        self.recorder.setEncodingSettings(settings)
        self.recorder.setContainerFormat('audio/x-wav')
        self.recorder.setOutputLocation(qtc.QUrl.fromLocalFile(audiofile2))

        #Record Button
        self.record_button = RecordButton()
        self.layout().addWidget(self.record_button, 4, 0, 1, 2)
        self.recorder.stateChanged.connect(self.record_button.on_state_changed)
        self.record_button.clicked.connect(self.on_recordbutton)
        self.shortcut = qtw.QShortcut(qtg.QKeySequence("Space"), self)
        self.shortcut.activated.connect(self.on_recordbutton)

        #Send Order Button
        self.sendorder_button = SendOrderButton()
        self.sendorder_button.setShortcut(qtg.QKeySequence('Tab'))
        self.layout().addWidget(self.sendorder_button, 5, 0, 1, 2)
        #self.sendorder_button.clicked.connect(qtc.QCoreApplication.instance().quit)
        #self.sendorder_button.clicked.connect(qtc.QCoreApplication.exit(0))

    def on_playbutton(self):
        if self.player.state() == qtmm.QMediaPlayer.PlayingState:
            self.player.stop()
        else:
            self.player.play()

    def set_file(self, url):
        self.label.setText(url.fileName())
        if url.scheme() == '':
            url.setScheme('file')
        content = qtmm.QMediaContent(url)
        self.player.setMedia(content)

    def get_file(self):
        fn, _ = qtw.QFileDialog.getOpenFileUrl(
            self,
            "Select File",
            qtc.QDir.homePath(),
            "Audio files (*.wav *.flac *.mp3 *.ogg *.aiff);; All files (*)"
        )
        if fn:
            self.set_file(fn)

    def on_recordbutton(self):
        if self.recorder.state() == qtmm.QMediaRecorder.RecordingState:
            self.recorder.stop()
            url = self.recorder.actualLocation()
            self.set_file(url)
        else:
            self.recorder.record()

def main():
    #app = qtw.QApplication(sys.argv)
    window = MainWindow()
    timestamp = time.strftime('%H:%M:%S')
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    #window.show()
    #app.exec_()
    return window, timestamp

if __name__ == '__main__':
    import sys

    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    window.show()
    sys.exit(app.exec_())