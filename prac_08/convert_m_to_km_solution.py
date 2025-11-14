"""
CP1404 Prac
Convert Miles to Kilometres
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesConverterApp(App):

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km_solution.kv')
        return self.root

    def handle_calculate(self):
        miles = self.get_validated_miles()
        km = miles * MILES_TO_KM
        self.root.ids.output_label.text = f"{km:.3f}"

    def handle_increment(self, amount):
        miles = self.get_validated_miles() + amount
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

    def get_validated_miles(self):
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
