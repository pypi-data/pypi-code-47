import keyboard
import logkit


class AppMenu:
    def __init__(self, items):
        print("You made a menu!")
        self.items = items
        self.selected_index = 0
        self.show(self.items, self.selected_index)

    def show(self, items, selected_index):
        for i, item in enumerate(items):
            is_selected = i == selected_index
            self.show_single_item(item, is_selected)

    def interact(self):
        keyboard.add_hotkey('up', self.up)
        keyboard.add_hotkey('down', self.down)
        keyboard.wait()

    @staticmethod
    def show_single_item(name, selected):
        if selected:
            print("> " + name)
        else:
            print(name)

    def up(self):
        self.selected_index += 1
        self.show(self.items, self.selected_index)

    def down(self):
        self.selected_index -= 1
        self.show(self.items, self.selected_index)
