import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

UI = "App.glade"

class Main:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(UI)
        self.builder.connect_signals(self)
        applyButton = self.builder.get_object("btnApply")
        applyButton.connect("clicked", self.applyButtonClicked)
        window = self.builder.get_object("window")
        applyButton.connect("clicked", self.applyButtonClicked)
        window.show()

def applyButtonClicked(self, widget):
    print("Applied")