from tkinter import *
from creational.Singleton import Singleton
import eqs_window, footerwindow


class Window(Tk, Singleton):
    def init(self):
        print('calling from init')
        super().__init__()

        self.button = Button(self, text = 'open eqs window', command = self.create_window_eqs)
        self.button.pack(expand=True)

        self.button = Button(self, text = 'creater footer eqs', command=self.create_footer_eqs)
        self.button.pack(expand=True)

    def create_window_eqs(self):
        global extraWindow
        extraWindow = eqs_window.Extra()

    def create_footer_eqs(self):
        global extraWindow
        extraWindow = footerwindow.Extra()

    def __init__(self):
        print('calling from __init__')

