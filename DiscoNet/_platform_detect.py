import sys, os
from subprocess import call as subcall

class Detect():
    doc_path = ''
    icon = ''
    def open_method(filename):
        pass


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

if sys.platform.startswith('win'):
    import winshell
    def win_open(filename):
        os.startfile(filename)
    Detect.open_method = win_open
    Detect.icon = resource_path('disco.ico')
    Detect.doc_path = winshell.my_documents()
else:
    Detect.doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
    if sys.platform.startswith('darwin'):
        def darwin_open(filename):
            subcall(('open', filename))
        Detect.open_method = darwin_open
        Detect.icon = resource_path('disco-1024.png')
    else:
        Detect.icon = resource_path('disco-256.png')
        if os.name == 'posix':
            def posix_open(filename):
                subcall(('xdg-open', filename))
            Detect.open_method = posix_open
