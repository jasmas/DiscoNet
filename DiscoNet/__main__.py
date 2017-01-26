#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DiscoNet GUI Application
"""


import sys, os
from multiprocessing import freeze_support
from DiscoNet.discoveryscan import DiscoveryScan

# freeze support
# Module multiprocessing is organized differently in Python 3.4+
try:
    # Python 3.4+
    if sys.platform.startswith('win'):
        import multiprocessing.popen_spawn_win32 as forking
    else:
        import multiprocessing.popen_fork as forking
except ImportError:
    import multiprocessing.forking as forking

if sys.platform.startswith('win'):
    # First define a modified version of Popen.
    class _Popen(forking.Popen):
        def __init__(self, *args, **kw):
            if hasattr(sys, 'frozen'):
                # We have to set original _MEIPASS2 value from sys._MEIPASS
                # to get --onefile mode working.
                os.putenv('_MEIPASS2', sys._MEIPASS)
            try:
                super(_Popen, self).__init__(*args, **kw)
            finally:
                if hasattr(sys, 'frozen'):
                    # On some platforms (e.g. AIX) 'os.unsetenv()' is not
                    # available. In those cases we cannot delete the variable
                    # but only set it to the empty string. The bootloader
                    # can handle this case.
                    if hasattr(os, 'unsetenv'):
                        os.unsetenv('_MEIPASS2')
                    else:
                        os.putenv('_MEIPASS2', '')

    # Second override 'Popen' class with our modified version.
    forking.Popen = _Popen


if __name__ == '__main__':
    freeze_support()

import sys, os, subprocess, ipaddress
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.lang import Builder


class ValidatingTextInput(TextInput):
    def __init__(self, **kwargs):
        super(ValidatingTextInput, self).__init__(**kwargs)

    def on_focus(self, obj, focused):
        if not focused:
            self.dispatch('on_text_validate')


class SelectDialog(FloatLayout):
    select = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)
    path = ObjectProperty(None)
    file = ObjectProperty(None)


class Root(FloatLayout):
    file_name = ObjectProperty(None)
    networks = ObjectProperty(None)
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    commands = ObjectProperty(None)
    if sys.platform.startswith('win'):
        import winshell
        default_name = os.path.join(winshell.my_documents(), 'Discovery.xlsx')
    else:
        default_name = os.path.join(os.path.expanduser('~'), 'Documents',
                                    'Discovery.xlsx')

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_select(self):
        content = SelectDialog(select=self.select, cancel=self.dismiss_popup,
                               path=os.path.dirname(self.file_name.text),
                               file=os.path.basename(self.file_name.text))
        self._popup = Popup(title="Select Discovery File", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def select(self, path, filename):
        if not filename.endswith('.xlsx'):
            filename+='.xlsx'
        self.file_name.text = os.path.join(path, filename)

        self.dismiss_popup()

    def invalid_networks(self, context):
        self.dismiss_popup()
        self.networks.focus = True
        self.networks.select_all()

    def validate_networks(self, nets):
        try:
            for net in nets.split(','):
                net = ipaddress.ip_network(net)
        except:
            content_cancel = Button(text='Dismiss', size_hint_y=None, height=40)
            content_label = Label(text="Networks must be a comma delimited list of "
                                       "networks and IP addresses, e.g.,\n'10.0.0.0/16,"
                                       "192.168.0.0/255.255.255.0,10.10.10.10'")
            content = BoxLayout(orientation='vertical')
            content.add_widget(content_label)
            content.add_widget(content_cancel)
            self._popup = Popup(title="Invalid Networks", content=content,
                                size_hint=(0.7, 0.3), auto_dismiss=False)
            content_cancel.bind(on_release=self.invalid_networks)
            self._popup.open()

    def finish_discovery(self):
        self.dismiss_popup()
        if sys.platform.startswith('darwin'):
            subprocess.call(('open', self.file_name.text))
        elif os.name == 'nt':
            os.startfile(self.file_name.text)
        elif os.name == 'posix':
            subprocess.call(('xdg-open', self.file_name.text))

    def run_discovery(self):
        self._popup = Popup(title="Discovery", content=Label(text="Running..."),
                            size_hint=(0.7, 0.3), auto_dismiss=False)
        self._popup.open()
        d = DiscoveryScan(self.file_name.text, self.networks.text, self.username.text,
                          self.password.text, self.commands.text)
        d.start(self.finish_discovery)


root = Builder.load_string("""
#:kivy 1.1.0

<RowLayout@BoxLayout>:
    source: None    
    size_hint_y: None
    height: 60

<MyLabel@Label>:
    source: None
    size_hint_x: 0.2
    text_size: self.size
    halign: 'right'
    valign: 'middle'
    padding: (10, 10)

<MyButton@Button>:
    source: None
    size_hint_x: 0.8
    text_size: self.size
    halign: 'center'
    valign: 'middle'
    padding: (10, 10)

<MyTextInput@TextInput>:
    source: None
    size_hint_x: 0.8
    multiline: False
    halign: 'left'
    valign: 'middle'
    padding: (10, 10, 10, 10)
    write_tab: False

Root:
    file_name: file_name
    networks: networks
    username: username
    password: password
    commands: commands
    BoxLayout:
        orientation: 'vertical'
        RowLayout:
            MyLabel:
                text: 'Discovery File:'
            MyButton:
                id: file_name
                halign: 'left'
                text: root.default_name
                on_release: root.show_select()
        RowLayout:
            MyLabel:
                text: 'Networks:'
            ValidatingTextInput:
                id: networks
                size_hint_x: 0.8
                multiline: False
                halign: 'left'
                valign: 'middle'
                padding: (10, 10, 10, 10)
                write_tab: False
                hint_text: '10.0.0.0/24,10.10.10.10,172.16.21.42'
                on_text_validate: root.validate_networks(networks.text)
        RowLayout:
            MyLabel:
                text: 'Username:'
            MyTextInput:
                id: username
                hint_text: 'admin'
        RowLayout:
            MyLabel:
                text: 'Password:'
            MyTextInput:
                id: password
                password: True
        BoxLayout:
            MyLabel:
                valign: 'top'
                text: 'Commands:'
            MyTextInput:
                id: commands
                multiline: True
                hint_text: "show ver\\nshow run\\nshow ip int br"
        RowLayout:
            MyButton:
                size_hint_x: 0.2
                text: 'Quit'
                on_release: app.stop()
            MyButton:
                text: 'Run Discovery'
                on_release: root.run_discovery()

<SelectDialog>:
    text_input: text_input
    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "vertical"
        FileChooserListView:
            id: filechooser
            path: root.path
            filters: ['*.xlsx']
            on_selection: text_input.text = self.selection and self.selection[0] or 'Discovery.xlsx'

        TextInput:
            id: text_input
            size_hint_y: None
            height: 60
            multiline: False
            write_tab: False
            text: root.file

        RowLayout:
            Button:
                text: "Cancel"
                on_release: root.cancel()

            Button:
                text: "Select"
                on_release: root.select(filechooser.path, text_input.text)

""")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.dirname(__file__))

    return os.path.join(base_path, relative_path)

class DiscoNet(App):
    def build(self):
        self.icon = resource_path('disco.ico')
        return root


Factory.register('Root', cls=Root)
Factory.register('SelectDialog', cls=SelectDialog)

def run():
    DiscoNet().run()

if __name__ == '__main__':
    freeze_support()
    run()
