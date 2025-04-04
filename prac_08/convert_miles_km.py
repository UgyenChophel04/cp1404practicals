from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934  # Conversion constant

class MilesConverterApp(App):
    output_text = StringProperty('0.0')  # StringProperty for dynamic updates

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation of miles to kilometres based on input."""
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0.0
        km = miles * MILES_TO_KM
        self.output_text = f"{km:.3f}"

    def handle_increment(self, change):
        """Increment or decrement the miles value by the given change."""
        try:
            current_miles = float(self.root.ids.input_miles.text)
        except ValueError:
            current_miles = 0.0
        new_miles = current_miles + change
        self.root.ids.input_miles.text = f"{new_miles}"

MilesConverterApp().run()