""" @author Kelsey Kopper
A program to convert text files using custom generated cipher libraries.

This program is used to encode and decode text files using randomized
substitution ciphers. Ciphers are generated by creating a mapping from each ASCII
character to a random Unicode character. The mappings are then stored in .json
files in the lib/ folder, where they can be located and reused to convert files
repeatedly.

"""

import os
import kivy
import cipher as c
kivy.require('2.3.0') 

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

# TODO - set window name to change when a file is selected
# TODO - add scroll bar to file contents window 
# TODO - proper google documentation style

class LoadDialog(FloatLayout):
    """ @brief Class for handling file opening/closing. """
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Cipher(BoxLayout):
    """ @brief Class for handling the program contents and functionality. """
    
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
        """ @brief Update displayed notification
            @param msg Type string contains message to display in notif. box.
        """
        self.update_msg.text = msg

    def display_file(self, file):
        """ @brief Open file to convert and display its contents. 
            @param file Type string contains path to text file to display.
        """
        with open(file, 'r') as f:
            self.file_display.text = f.read()

    def get_lib(self, name):
        """ @brief Locate/create cipher library from given name. 
            @param name Type string contains keyword name of the cipher library.
        """
        self.cipher_map.set_name(name)

        if self.cipher_map.already_exists(): 
            self.cipher_map.read_map()
            self.set_update("Located preexisting library.")
        else: 
            self.cipher_map.create_cipher()
            self.set_update("Unable to locate preexissting library. Created new library under this name")

    def set_mode(self, mode):
        """ @brief Set file conversion mode. 
            @param mode Type string contains file conversion mode type 
                (encode or decode)
        """
        self.mode = mode

    def dismiss_popup(self):
        """ @brief Dismiss a popup. """
        self._popup.dismiss()

    def show_load(self):
        """ @brief Open the file chooser menu. """
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(content=content)
        self._popup.open()

    def load(self, path, file):
        """ @brief Open a file from the file chooser menu, display its contents 
            and then close the menu. 
            @param path Type string contains path to file to open
            @param file Type string contains name of file to open
        """
        file = os.path.join(path, file[0])
        self.file_name = file
        self.display_file(file)

        self.dismiss_popup()
        
    def convert(self):
        """ @brief Convert a file. """
        # handle error checking, make sure all fields are set
        if self.file_name != '' and self.mode != '' and self.cipher_map.name_is_set:
            self.cipher_map.code_file(self.file_name, self.mode)
            self.display_file(self.file_name)
        else:
            self.set_update("Error: complete all fields before attempting to convert file.")

class CipherApp(App):
    """ @brief Class to handle program wrapper. """
    def build(self):
        return Cipher()
    
if __name__ == '__main__':
    CipherApp().run()