import socketio

sio = socketio.Client()

class Connection():
    def __init__(self, project_name="", description="", author="", link="", url="", passcode=""):
        
        # Default behavior
        self.fnDict = {}
        self.sio = sio
        self.project_name = project_name
        self.description = description
        self.author = author
        self.link = link

        if project_name == "":
            raise ValueError("Please specify your project name")
            pass
        if url == "" and passcode == "":
            # Free usage of spineapi.com
            raise ValueError("Please enter your passcode")
            pass
        elif url == "":
            # Paid usage of spineapi.com
            raise ValueError("Please enter your server url")
            pass
        elif passcode == "":
            # Self hosting, but you have to pass in the authcode of your server.
            raise ValueError("You're choosing to self host the server. Please enter your passcode.")
        else:
            # Self hosting
            self.url = url
            self.passcode = passcode
    
    def register_function(self, pathname="", requiresAuth=False, authToken="", function=lambda *args: None):
        self.fnDict[pathname] = {
            'requiresAuth': requiresAuth,
            'authToken': authToken,
            'function': function,
        }
        pass
    
    def run(self):
        try:
            self.sio.connect(self.url + '?passcode=' + self.passcode)
            # Default behavior
            @sio.event
            def connect():
                print("I'm connected")
                self.sio.emit("update_project_info", {
                    "project_name": self.project_name,
                    "description": self.description,
                    "author": self.author,
                    "link": self.link,
                })
                for pathname in self.fnDict:
                    self.sio.emit("register_path", {
                        'pathname': pathname,
                        'requiresAuth': self.fnDict[pathname]['requiresAuth'],
                        'authToken': self.fnDict[pathname]['authToken'],
                    })

            @sio.event
            def connect_error():
                print("The connection failed!")

            @sio.event
            def disconnect():
                print("I'm disconnected!")

            # Main behavior
            @sio.event
            def register_path(data):
                if data["result"] == "success":
                    @sio.on(data["pathname"])
                    def on_message(message):
                        output = self.fnDict[data["pathname"]]["function"](message["input"])
                        self.sio.emit(message["requestUUID"], output)
                else:
                    print(data["errorMessage"])
        except Exception as e:
            print(e)