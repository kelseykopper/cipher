# @author Kelsey Kopper
import sys
import string
import cipher as c

# if __name__ == '__main__':
#   c_map = c.CipherMap("hw1")
#   c_map.create_cipher()
#   c_map.code_file("tests/hw1.txt", "encrypt")

# really only need a couple pieces of info from ui:
# mode -> encrypt or decrypt (maybe have selection option for this)
# cipher lib name -> text box
  # should program automatically search for lib with this name? 
  # maybe then if it doesn't find a lib with that name, generate new one
# file to encode/decode


# \venv\share\kivy-examples\demo\showcase\main.py
# showcase -> ToggleButton (for encode/decode)
# showcase -> RstDocument
# showcase -> Popups
# showcase -> FileChoosers (maybe this or somethign that actually opens)
# showcase -> Splitter (to resize document)
# showcase -> TextInputs (to enter lib name)

import kivy
kivy.require('2.3.0') 

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MainMenu(GridLayout):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Cipher library name'))
        self.lib_name = TextInput(multiline=False)

        self.add_widget(self.lib_name)
        # self.add_widget(Label(text='File'))
        # self.password = TextInput(password=True, multiline=False)
        # self.add_widget(self.password)


class CipherApp(App):

    def build(self):
        return MainMenu()


if __name__ == '__main__':
    CipherApp().run()