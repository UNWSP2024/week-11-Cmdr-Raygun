# Author: Andrew Bittner
# Date: 11/15/2024
# Program #2: Info Printer

import tkinter

class InfoWindow:
    def __init__(self):
        # Initialize text values.
        self.info = ('Andrew Bittner\n8990 Tamarack St NW\nCoon Rapids, MN '
                     '55433')

        # Define window settings.
        self.window = tkinter.Tk()
        self.window.title('Personal info')
        self.frame_top = tkinter.Frame(self.window, borderwidth =
                                       3, relief = 'groove')
        self.frame_bottom = tkinter.Frame(self.window)
        self.msg = tkinter.Message(self.frame_top, text = self.info, width =
                                   128)
        self.button_info = tkinter.Button(self.frame_bottom, text ='Show info'
                                          , command = self.show_info)
        self.button_exit = tkinter.Button(self.frame_bottom, text ='Exit',
                                          command = self.window.destroy)

        # Create window.
        self.button_info.pack(side = 'left', padx = 16)
        self.button_exit.pack(side = 'left', padx = 16)
        self.frame_top.pack(padx = 32, pady = (32, 16))
        self.frame_bottom.pack(padx = 32, pady = (16, 32))
        tkinter.mainloop()

    def show_info(self):
        # Display message only when show_info is called.
        self.msg.pack()

if __name__ == '__main__':
    window1 = InfoWindow()
                                                                               # No line should go beyond this point.