from logkit import log
from cli.app_menu import AppMenu


class AppInterface:
    def __init__(self):
        log.info("Welcome to the interface.")
        pass

    def start(self):
        log.info("Starting App Interface.")
        # input("Please Enter: ")
        menu = AppMenu(["item1", "item2", "item3"])
        menu.interact()
        pass
