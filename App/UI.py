import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
UI_FILE="UI.xml"
class UI:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(UI_FILE)
        self.builder.connect_signals(self)
        
        self.window = self.builder.get_object("window")
        self.window_label = self.builder.get_object("Controller")
        self.window.show_all()
        
    def button_clicked(self,Apply):
        self.Entry = self.builder.get_object("Entry")
        self.Vout = float(self.Entry.get_text())
        print (self.Vout)
        
        self.Vout1=self.builder.get_object("V_out")
        self.Vout1.set_text(str(2))
        
        
        self.Current=self.builder.get_object("Current")
        self.Current.set_text(str(1))
        
        self.power_consumption=self.builder.get_object("power_consumption")
        self.power_consumption.set_text(str(3))
        
    def windows_destroy(self,window):
        Gtk.main_quit()
            
    def main(self):
        Gtk.main()
            
if __name__=="__main__":
    ui = UI()
    ui.main()
        
