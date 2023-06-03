import gi
import subprocess

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk, GObject, AppIndicator3


class RedshiftControl:
    def __init__(self):
        self.indicator = AppIndicator3.Indicator.new(
            "redshift-indicator",
            "redshift-status-off",
            AppIndicator3.IndicatorCategory.APPLICATION_STATUS
        )
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.create_menu())

        # Create the Gtk window
        self.window = Gtk.Window()
        self.window.set_title("Redshift Control")
        self.window.set_default_size(400, 100)  # Set the width and height
        self.window.set_border_width(10)
        self.window.connect("delete-event", self.on_window_delete_event)

        # Close Button
        close_button = Gtk.Button(label="Close")
        close_button.connect("clicked", self.on_close_button_clicked)

        # Color Temperature Range Bar
        self.temp_adjustment = Gtk.Adjustment(3500, 1200, 6000, 100, 100, 0)
        self.temp_scale = Gtk.Scale(
            orientation=Gtk.Orientation.HORIZONTAL, adjustment=self.temp_adjustment
        )
        self.temp_scale.set_digits(0)
        self.temp_scale.set_value_pos(Gtk.PositionType.RIGHT)
        self.temp_scale.set_hexpand(True)
        self.temp_scale.set_valign(Gtk.Align.CENTER)
        self.temp_scale.set_margin_right(10)
        self.temp_scale.connect("value-changed", self.on_temp_scale_value_changed)

        self.label_temp = Gtk.Label(label="Color Temperature (K):")
        self.label_temp.set_valign(Gtk.Align.CENTER)

        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(10)
        self.grid.attach(self.label_temp, 0, 0, 1, 1)
        self.grid.attach(self.temp_scale, 1, 0, 1, 1)
        self.grid.attach(close_button, 0, 1, 2, 1)

        self.window.add(self.grid)
        self.window.show_all()

        # Apply the default color temperature
        self.apply_color_temperature()

    def create_menu(self):
        menu = Gtk.Menu()

        # Toggle Button
        toggle_item = Gtk.CheckMenuItem("Redshift On/Off")
        toggle_item.connect("toggled", self.on_toggle_item_toggled)
        toggle_item.set_active(True)
        menu.append(toggle_item)

        # Preferences
        preferences_item = Gtk.MenuItem("Preferences")
        preferences_item.connect("activate", self.on_preferences_item_activate)
        menu.append(preferences_item)

        # Quit
        quit_item = Gtk.MenuItem("Quit")
        quit_item.connect("activate", self.on_quit_item_activate)
        menu.append(quit_item)

        menu.show_all()
        return menu

    def on_toggle_item_toggled(self, toggle_item):
        if toggle_item.get_active():
            self.apply_color_temperature()
            self.indicator.set_icon("redshift-status-on")
        else:
            subprocess.run(['redshift', '-x'])
            self.indicator.set_icon("redshift-status-off")

    def on_temp_scale_value_changed(self, temp_scale):
        self.apply_color_temperature()

    def apply_color_temperature(self):
        temperature = int(self.temp_scale.get_value())
        subprocess.run(['redshift', '-P', '-O', str(temperature)])

    def on_window_delete_event(self, widget, event):
        Gtk.main_quit()

    def on_quit_item_activate(self, menu_item):
        Gtk.main_quit()

    def on_preferences_item_activate(self, menu_item):
        if self.window.get_visible():
            self.window.hide()
        else:
            self.window.present()

    def on_close_button_clicked(self, button):
        self.window.hide()


if __name__ == "__main__":
    GObject.threads_init()
    Gtk.init([])
    RedshiftControl()
    Gtk.main()
