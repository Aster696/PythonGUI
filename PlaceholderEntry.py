from tkinter import *

class PlaceholderEntry(Entry):
    def __init__(self, master=None, placeholder='', color='grey', *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.insert('0', self.placeholder)
        self.bind('<FocusIn>', self.on_focus_in)
        self.bind('<FocusOut>', self.on_focus_out)

    def on_focus_in(self, event):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self.config(fg='black')

    def on_focus_out(self, event):
        if not self.get():
            self.insert("0", self.placeholder)
            self.config(fg=self.placeholder_color)