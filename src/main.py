# @author Kelsey Kopper
import sys
import string
import cipher as c


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
from kivy.uix.button import Button 
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView

# def on_enter(instance):
#     print('User pressed enter in', instance)
#     print("With value ", instance.text)


# class InteractPanel(BoxLayout): 
#     def __init__(self, **kwargs):
#         super(InteractPanel, self).__init__(**kwargs)
#         self.orientation='vertical'

#         self.add_widget(Label(text='testing testing'))
#         self.add_widget(Label(text='WHO ARE YOU'))

#         self.add_widget(Label(text='Cipher library name'))
#         self.lib_name = TextInput(multiline=False)

#         self.lib_name.bind(on_text_validate=on_enter)

#         self.add_widget(self.lib_name)

#     def get_file_data(self):
#         """ Get file data """
#         return "teehee nothing here"


# class MainMenu(BoxLayout):
#     def __init__(self, **kwargs):
#         super(MainMenu, self).__init__(**kwargs)
#         self.orientation='horizontal'

#         # left panel for selecting settings related to cipher
#         self.interact_panel = InteractPanel()
#         self.add_widget(self.interact_panel)

#         # TODO: right panel should display file contents if available
#         file_data = self.interact_panel.get_file_data()
#         self.add_widget(Label(text=file_data))

class CipherApp(App):
    def __init__(self, **kwargs):
        super(CipherApp, self).__init__(**kwargs)
        self.c_map = c.CipherMap()
        self.file_name = ""
        self.file_contents = Label(text="")

    def open_file(self):
        pass

    def on_enter(self, instance):
        """ Set the cipher library name when enter key is pressed in text box. """
        self.c_map.set_name(instance.text)

    def show_file_chooser(self, instance):
        filechooser = FileChooserListView()
        
        content = BoxLayout(orientation='vertical')
        content.add_widget(filechooser)
        
        open_btn = Button(text="Open", size_hint=(1, 0.1))
        content.add_widget(open_btn)
        
        self.popup = Popup(title="Choose file to convert", content=content,
                           size_hint=(0.9, 0.9))
        
        open_btn.bind(on_press=lambda _: self.open_selected(filechooser.selection))
        
        self.popup.open()

    def open_selected(self, selection):
        if selection:
            self.file_name = selection[0]
            # TODO: figure out how to display unicode characters
            with open(self.file_name, 'r', encoding="utf-8") as file: 
                self.file_contents.text = file.read()

            print(f'Selected file: {selection[0]}')

        else:
            print('No file selected.')
        self.popup.dismiss()

    def build(self):
        wid = Widget()

        lib_inputbox = TextInput(multiline=False)
        lib_prompt = Label(text="Cipher library name")
        label2 = Label(text = 'goodbye world')

        btn_file = Button(text='Open file to convert', on_press=self.show_file_chooser)

        lib_inputbox.bind(on_text_validate=lambda instance: self.on_enter(instance))

        # TODO: make root and interact_panel not overlap
        interact_panel = BoxLayout(orientation='vertical')
        interact_panel.add_widget(lib_prompt)
        interact_panel.add_widget(lib_inputbox)
        interact_panel.add_widget(btn_file)
        interact_panel.add_widget(label2)

        root = BoxLayout(orientation='horizontal')
        root.add_widget(interact_panel)
        root.add_widget(self.file_contents)
        return root


if __name__ == '__main__':
    CipherApp().run()