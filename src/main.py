""" 
@author Kelsey Kopper
@brief Classes and methods for handling frontend.
"""

import os
import kivy
import cipher as c
kivy.require('2.3.0') 

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.properties import ObjectProperty

# TODO - set window name to change when a file is selected
# TODO - add scroll bar to file contents window 
# TODO - proper google documentation style

class LoadDialog(FloatLayout):
    """ Class for handling file opening/closing """
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Cipher(BoxLayout):
    
    color_palette = {
        "beige" : [0.9372549019607843, 0.8509803921568627, 0.7058823529411765, 1],
        "pink" : [0.8392156862745098, 0.6509803921568628, 0.5725490196078431, 1],
        "purple" : [0.6392156862745098, 0.5647058823529412, 0.5058823529411764, 1],
        "blue" : [0.30196078431372547, 0.3803921568627451, 0.3764705882352941, 1],
        "black" : [0.1607843137254902, 0.1450980392156863, 0.13333333333333333, 1]
    }
    
    # file to convert
    file_display = ObjectProperty()

    # name of cipher library
    lib_inpt = ObjectProperty() 

    # notification box relating to file I/O
    update_msg = ObjectProperty()

    # attributes relating to cipher obj + file conversion
    cipher_map = c.CipherMap()
    mode = ''
    file_name = ''

    def set_update(self, msg):
        """ Change notification box. """
        self.update_msg.text = msg

    def display_file(self, file):
        """ Open file to convert and display its contents. """
        with open(file, 'r') as f:
            self.file_display.text = f.read()

    def get_lib(self, name):
        """ Locate/create cipher library from given name. """
        self.cipher_map.set_name(name)

        if self.cipher_map.already_exists(): 
            self.cipher_map.read_map()
            self.set_update("Located preexisting library.")
        else: 
            self.cipher_map.create_cipher()
            self.set_update("Unable to locate preexissting library. Created new library under this name")

    def set_mode(self, mode):
        """ Set file conversion mode. """
        self.mode = mode

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(content=content)
        self._popup.open()

    def load(self, path, file):
        file = os.path.join(path, file[0])
        self.file_name = file
        self.display_file(file)

        self.dismiss_popup()
        
    def convert(self):
        """ Function to perform file conversion. """
        if self.file_name != '' and self.mode != '' and self.cipher_map.name_is_set:
            self.cipher_map.code_file(self.file_name, self.mode)
            self.display_file(self.file_name)
        else:
            self.set_update("Error: complete all fields before attempting to convert file.")

class CipherApp(App):

    def build(self):
        return Cipher()
    
if __name__ == '__main__':
    CipherApp().run()