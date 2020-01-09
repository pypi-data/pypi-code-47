from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.factory import Factory
from kivy.uix.floatlayout import FloatLayout
import Utilities as Ut
import os
import FullClient as fc

client = None
worker = None
Removegrid = None  # grid for remove function


class VerifyConnection(Screen):

    def CheckConnection(self):
        global client
        global worker
        client = fc.FullClient()
        worker = client.GetClientInstance()
        if not Ut.ConnectionEstabilished:
            invalidConnection()
        else:
            sm.current = "login"


class CreateAccountWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    Ut.clientusername = username
    Ut.clientpassword = password

    def submit(self):
        if self.username.text != "":
            if self.password.text != "":
                worker.RegisterClient(self.username.text, self.password.text)
                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.username.text = ""
        self.password.text = ""


class LoginWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    Ut.clientusername = username
    Ut.clientpassword = password

    def loginBtn(self):
        worker.LogInClient(self.username.text, self.password.text)
        while Ut.ReceivedAnswer is False:
            pass
        Ut.ReceivedAnswer = False
        if Ut.LoggedIn:
            Ut.LoggedIn = False
            Ut.clientusername = None
            Ut.clientpassword = None
            Ut.clientusername = self.username.text
            Ut.clientpassword = self.password.text
            self.reset()
            sm.current = "work"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.username.text = ""
        self.password.text = ""


class MainWindow(Screen):
    username = ObjectProperty(None)
    created = ObjectProperty(None)
    Ut.clientusername = username

    current = ""

    def logOut(self):
        sm.current = "login"


class WindowManager(ScreenManager):
    pass


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class WorkWindow(Screen):
    current = ""

    loadfile = ObjectProperty(None)

    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Upload file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        if len(filename) == 0:  # este folder
            if path != "/":
                worker.uploadFolder(path)
            return

        else:
            with open(os.path.join(path, filename[0])) as stream:
                worker.send_File(filename[0])
                sm.current = "work"

    def show_download(self):

        self._popup = Popup(title="Download file", content=ScrollView(size_hint=(1, None), size=(500, 500)))
        self._popup.bind(on_open=self.download)
        self._popup.open()

    def CallbackDownload(self, instance):
        worker.downloadFile(instance.text[1:], Ut.clientusername, Ut.clientpassword)

    def download(self, instance):
        buttons = []

        worker.list_uploads(Ut.clientusername, Ut.clientpassword)
        while Ut.ReceivedAnswer is False:
            pass
        grid = GridLayout(rows=Ut.filelist.__len__(), spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        for i in Ut.filelist:
            button = Button(text=str(i), background_color=(1, 0, 1, 1), size_hint_y=None,
                            height=40)
            buttons.append(button)
        for button in buttons:
            button.bind(on_release=self.CallbackDownload)
            grid.add_widget(button)
        instance.content.add_widget(grid)
        Ut.ReceivedAnswer = False
        sm.current = "work"

    def show_remove(self):

        self._popup = Popup(title="Remove file", content=ScrollView(size_hint=(1, None), size=(500, 500)))
        self._popup.bind(on_open=self.remove)
        self._popup.open()

    def CallbackRemove(self, instance):
        global Removegrid
        worker.removeFile(instance.text[1:])
        Ut.filelist.remove(instance.text)
        Removegrid.remove_widget(instance)

    def remove(self, instance):
        global Removegrid

        worker.list_uploads(Ut.clientusername, Ut.clientpassword)
        while Ut.ReceivedAnswer is False:
            pass

        Removegrid = GridLayout(rows=Ut.filelist.__len__(), spacing=10, size_hint_y=None)
        Removegrid.bind(minimum_height=Removegrid.setter('height'))
        for i in Ut.filelist:
            button = Button(text=str(i), background_color=(1, 0, 1, 1), size_hint_y=None,
                            height=40, on_press=self.CallbackRemove)
            Removegrid.add_widget(button)
        instance.content.add_widget(Removegrid)
        Ut.ReceivedAnswer = False
        sm.current = "work"


Factory.register('LoadDialog', cls=LoadDialog)


def invalidLogin():
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()


def invalidConnection():
    pop = Popup(title='Invalid Connection',
                content=Label(text='Failed to connect to server!'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


kv = Builder.load_file("create.kv")

sm = WindowManager()

screens = [VerifyConnection(name="verify"), LoginWindow(name="login"), CreateAccountWindow(name="create"),
           MainWindow(name="main"), WorkWindow(name="work")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "verify"


class UnixDriveApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    UnixDriveApp().run()
