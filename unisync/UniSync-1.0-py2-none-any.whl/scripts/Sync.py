from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import Client as sync
from kivy.factory import Factory
from kivy.uix.floatlayout import FloatLayout
import Utilities as Ut
import os

SyncClient = None
ClientWorker = None
Removegrid = None


class VerifyConnection(Screen):

    def CheckConnection(self):
        global SyncClient
        global ClientWorker
        SyncClient = sync.SyncClient()
        ClientWorker = SyncClient.GetClientInstance()
        if not Ut.ConnectionEstabilished:
            invalidConnection()
        else:
            sm.current = "login"


class CreateAccountWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    Ut.clientusername = username
    Ut.clientpassword = password

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.username.text = ""
        self.password.text = ""


class LoginWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    Ut.username = username
    Ut.password = password

    def loginBtn(self):
        Ut.username = self.username.text
        Ut.password = self.password.text
        if Ut.username == "" or Ut.password == "":
            invalidLogin()
            return
        ClientWorker.Login()
        while Ut.AnswerReceived is False:
            pass
        Ut.AnswerReceived = False
        if Ut.LoggedIn is True:
            SyncClient.StartSyncThreads()
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


class WindowManager(ScreenManager):
    pass


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class WorkWindow(Screen):
    current = ""

    def show_remove(self):
        self._popup = Popup(title="Remove file", content=ScrollView(size_hint=(1, None), size=(500, 500)))
        self._popup.bind(on_open=self.remove)
        self._popup.open()

    def RemoveCallback(self, instance):
        global Removegrid
        ClientWorker.removeFile(instance.text)
        Ut.filelist.remove(instance.text)
        Removegrid.remove_widget(instance)

    def remove(self, instance):
        global Removegrid

        ClientWorker.listSyncFiles()
        while Ut.AnswerReceived is False:
            pass

        Removegrid = GridLayout(rows=Ut.filelist.__len__(), spacing=10, size_hint_y=None)
        Removegrid.bind(minimum_height=Removegrid.setter('height'))
        for i in Ut.filelist:
            button = Button(text=str(i), background_color=(1, 0, 1, 1), size_hint_y=None,
                            height=40)
            button.bind(on_press=self.RemoveCallback)
            Removegrid.add_widget(button)
        instance.content.add_widget(Removegrid)
        Ut.AnswerReceived = False
        sm.current = "work"

    loadfile = ObjectProperty(None)

    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_sync(self):
        content = LoadDialog(load=self.sync, cancel=self.dismiss_popup)
        self._popup = Popup(title="Sync file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def sync(self, path, filename):
        if len(filename) != 0:
            with open(os.path.join(path, filename[0])) as stream:
                ClientWorker.addFiletoServer(filename[0])
                sm.current = "work"
        return


Factory.register('LoadDialog', cls=LoadDialog)


def invalidLogin():
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidConnection():
    pop = Popup(title='Invalid Connection',
                content=Label(text='Failed to connect to server!'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


kv = Builder.load_file("createsync.kv")

sm = WindowManager()

screens = [VerifyConnection(name="verify"), LoginWindow(name="login"), CreateAccountWindow(name="create"),
           WorkWindow(name="work")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "verify"


class UniSyncApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    UniSyncApp().run()
