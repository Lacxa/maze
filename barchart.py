from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen


class Barchart(MDScreen):
    def set_text(self, args):
        self.ids._label.text = f"{args[1]} [{args[2]},{args[3]}]"

    def update(self):
        chart1 = self.ids.chart1
        chart1.x_values = [2, 8, 12, 35, 40, 43, 56]
        chart1.y_values = [3, 2, 1, 20, 0, 1, 10]
        chart1.update()

        chart2 = self.ids.chart2
        chart2.x_values = [2, 8, 12, 35, 40, 43, 56]
        chart2.y_values = [3, 2, 1, 20, 0, 1, 10]
        chart2.update()

        chart3 = self.ids.chart3
        chart3.x_labels = ["XYZ", "Second", "Third", "Last"]
        chart3.y_labels = ["XYZ", "Second", "Third", "Last"]
        chart3.update()

