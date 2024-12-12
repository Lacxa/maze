from kivy.lang import Builder
from kivymd.app import MDApp

# KivyMD code for the icons and labels
kv_code = """
BoxLayout:
    orientation: "vertical"
    padding: 20
    spacing: 20

    BoxLayout:
        orientation: "horizontal"
        spacing: 10
        size_hint_y: None
        height: "50dp"

        MDIcon:
            icon: "school"
            size_hint: None, None
            size: "24dp", "24dp"

        MDLabel:
            text: "Schools"
            halign: "left"
            valign: "center"

    BoxLayout:
        orientation: "horizontal"
        spacing: 10
        size_hint_y: None
        height: "50dp"

        MDIcon:
            icon: "account-group"
            size_hint: None, None
            size: "24dp", "24dp"

        MDLabel:
            text: "Students"
            halign: "left"
            valign: "center"

    BoxLayout:
        orientation: "horizontal"
        spacing: 10
        size_hint_y: None
        height: "50dp"

        MDIcon:
            icon: "account"
            size_hint: None, None
            size: "24dp", "24dp"

        MDLabel:
            text: "Visitors"
            halign: "left"
            valign: "center"
"""

class IconApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(kv_code)

# Run the app
IconApp().run()
