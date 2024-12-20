from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen

Builder.load_string(
    """
<MyAKBarChart@AKBarChart>
    size_hint_y: None
    height: dp(180)
    x_values: [0, 5, 8, 15]
    y_values: [0, 10, 6, 8]
    label_size: dp(12)


<Barchart>
    on_leave: pass

    MDBoxLayout:
        orientation: "vertical"

        ScrollView:

            MDBoxLayout:
                orientation: "vertical"
                spacing: dp(25)
                padding: dp(25)
                adaptive_height: True
                
                MyAKBarChart:
                    id: chart3
                    labels: True
                    anim: True
                    x_labels: ["XYZ", "Second", "Third", "Last"]
                    y_labels: ["40", "30", "10", "20"]
                    bars_color:[0, 0, 0.4, 1]
                    labels_color:[0, 0, 0.4, 1]
                    lines_color: [0, 0, 0.4, 1]
                    on_select: root.set_text(args)


        MDBoxLayout:
            adaptive_height: True

            MDRaisedButton:
                text: "update"
                on_release: root.update()

     
"""
)


class Barchart(MDScreen):

    def update(self):

        chart3 = self.ids.chart3
        chart3.x_labels = ["XYZ", "Second", "Third", "Last"]
        chart3.y_values = [35, 40, 43, 56]
        chart3.update()
