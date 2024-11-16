# Author: Andrew Bittner
# Date: 11/15/2024
# Program #1: Wisdom of Thorin

import tkinter

class MsgWindow:
    def __init__(self):
        # Initialize text values.
        self.msg_text = '“If more of us valued food and cheer and song above hoarded gold, it would be a merrier world.”'
        self.label_text = '\n- Thorin Oakenshield'

        # Define window settings.
        self.window = tkinter.Tk()
        self.frame = tkinter.Frame(self.window)
        self.msg = tkinter.Message(self.frame, text = self.msg_text, font = ('High Tower Text', 20))
        self.label = tkinter.Label(self.frame, text = self.label_text, font = ('High Tower Text', 12, 'bold'))
        self.window.title('Words of Wisdom')

        # Create window.
        self.msg.pack()
        self.label.pack(side = 'right')
        self.frame.pack(padx = 32, pady = 32)
        self.frame.pack()
        tkinter.mainloop()

if __name__ == '__main__':
    window1 = MsgWindow()