import pyxhook
import os

from tkinter import *

root = Tk()
root.geometry('300x100')
root.title('key count')
root.resizable(0, 0)
# Allow clearing the log file on start, if pylogger_clean is defined.

keyboard_count = '{}.txt'.format('keyboard')
mouse_count = '{}.txt'.format('mouse')
# creating key pressing event and saving it into log file


def gui():
    root = Tk()
    root.geometry('300x100')
    root.title('key count')
    root.resizable(0, 0)
    key_count = get_key()
    T = Text(root, width=900, height=900, bg='khaki', borderwidth=0)
    T.pack()
    T.insert(END, "keyboard_count: {}, mouse_count: {}".format(key_count[0], key_count[1]))
    root.mainloop()


class App(object):
    def __init__(self, root):
        self.root = root
        self.txt_frm = Frame(self.root, width=900, height=900, bg='khaki')
        self.txt_frm.pack(fill="both", expand=True)
        button1 = Button(self.txt_frm, text="keyboard_count", command=self.keyboard_count, borderwidth=0)
        button1.grid(column=0, row=2, padx=2, pady=2)
        button2 = Button(self.txt_frm, text="mouse_count", command=self.mouse_count, borderwidth=0)
        button2.grid(column=1, row=2, padx=2, pady=2)
        self.entry_var = StringVar()
        entry = Entry(self.txt_frm, textvariable=self.entry_var, borderwidth=0)
        entry.grid(column=0, row=3, columnspan=2, padx=2, pady=2)

    def keyboard_count(self):
        key_count = get_key()[0]
        self.entry_var.set(key_count)

    def mouse_count(self):
        mou_count = get_key()[1]
        self.entry_var.set(mou_count)


def OnKeyPress(event):

    if 'mouse' in str(event):
        key = event.MessageName
        listener = mouse_count
    else:
        key = event.Key
        listener = keyboard_count
        if key == 'P_Add':
            gui()

    with open(listener, 'a') as f:
        f.write('{},'.format(key))

    # create a hook manager object


def get_key():
    keyboard_lis_count = 0
    mouse_lis_count = 0

    if os.path.exists(keyboard_count):
        keyboard_lis_count = list(filter(None, open(keyboard_count, 'r').read().split(',')))
        keyboard_lis_count = len(keyboard_lis_count)
    if os.path.exists(mouse_count):
        mouse_lis_count = list(filter(None, open(mouse_count, 'r').read().split(',')))
        mouse_lis_count = len(mouse_lis_count)

    return keyboard_lis_count, mouse_lis_count


def main():
    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = OnKeyPress
    new_hook.MouseAllButtonsDown = OnKeyPress
    # set the hook
    new_hook.HookKeyboard()
    try:
        if os.path.exists(keyboard_count):
            os.unlink(keyboard_count)
        if os.path.exists(mouse_count):
            os.unlink(mouse_count)
        new_hook.start()  # start the hook
        app = App(root)
        root.mainloop()
    except KeyboardInterrupt:
        # User cancelled from command line.
        pass
    except Exception as ex:
        # Write exceptions to the log file, for analysis later.
        msg = 'Error while catching events:\n {}'.format(ex)
        print(msg)
        # with open(log_file, 'a') as f:
        #     f.write('\n{}'.format(msg))


if __name__ == '__main__':
    main()


