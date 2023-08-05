#!/usr/bin/env python3

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

UI_FILE = "example.ui"


class Example:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(UI_FILE)
        self.builder.connect_signals(self)

        self.window = self.builder.get_object("window")
        self.window_label = self.builder.get_object("window_label")
        self.window.show_all()

    def button_clicked(self, button):
        self.window_label.set_text("You clicked!")

    def about_clicked(self, button):
        self.window_label.set_text("This is just an example.")

    def quit_clicked(self, button):
        self.on_window_destroy(self.window)

    def on_window_destroy(self, window):
        Gtk.main_quit()


def main():
    app = Example()
    Gtk.main()


if __name__ == "__main__":
    main()