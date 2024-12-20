import ast
import sys
from os import path

sys.path.append(path.join(path.abspath(__file__).rsplit("examples", 1)[0]))
from kivy.factory import Factory  # noqa
from kivy.lang import Builder  # noqa
from kivy.properties import StringProperty  # noqa
from kivymd.app import MDApp  # noqa
from kivymd.uix.list import OneLineAvatarListItem  # noqa
from kivymd.uix.toolbar import MDTopAppBar  # noqa

from kivymd_extensions.akivymd.uix.statusbarcolor import (  # noqa
    change_statusbar_color,
)

kv = """
#: import StiffScrollEffect kivymd.effects.stiffscroll.StiffScrollEffect

<IconListItem@OneLineAvatarListItem>:

    IconLeftWidget:
        icon: root.icon

<MyToolbar@MDTopAppBar>:
    left_action_items: [["arrow-left", lambda x: app.show_screen("Home", "back")]]


MDScreen:

    ScreenManager:
        id: screen_manager

        MDScreen:
            name: "Home"

            Image:
                source: "assets/logo.png"
                opacity: .3

            MDBoxLayout:
                orientation: "vertical"

                MyToolbar:
                    title: app.title
                    left_action_items:[["menu" , lambda x: navdrawer.set_state("open")]]

                BoxLayout:
                    padding:dp(20)

                    MDLabel:
                        text: app.intro
                        theme_text_color: "Primary"
                        halign: "center"

    MDNavigationDrawer:
        id: navdrawer

        ScrollView:
            # effect_cls: StiffScrollEffect
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True

                MDRelativeLayout:
                    size_hint_y: None
                    height: title_box.height

                    FitImage:
                        source: "assets/texture_blur.png"

                    MDBoxLayout:
                        id: title_box
                        adaptive_height: True
                        padding: dp(24)

                        MDLabel:
                            text: "Awesome KivyMD"
                            font_style: "H5"
                            size_hint_y: None
                            height: self.texture_size[1]
                            shorten: True

                MDList:
                    id: menu_list
"""


class IconListItem(OneLineAvatarListItem):
    icon = StringProperty()


class DemoApp(MDApp):

    intro = """Here is where you can find all of the widgets. take a look at
    screens folder to find examples of how to use them. I will gradually add
    more and more Awesome widgets to this project. Stay tuned!"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Teal"
        self.title = "Awesome KivyMD"
        change_statusbar_color(self.theme_cls.primary_color)

    def build(self):
        self.root = Builder.load_string(kv)

    def on_start(self):

        self.data_screens = {
                "Barchart": {
                    "import": "barchart",
                    "factory": "Barchart",
                    "screen_name": "barchart",
                }
            }

        data_screens = list(self.data_screens.keys())
        data_screens.sort()

        for list_item in data_screens:
            self.root.ids.menu_list.add_widget(
                IconListItem(
                    text=list_item,
                    icon="chart-bar",
                    on_release=lambda x=list_item: self.load_screen(),
                )
            )

    def load_screen(self):
        manager = self.root.ids.screen_manager

        if not manager.has_screen("barchart"):
            exec("from screens import %s" % "barchart")
            screen_object = eval("Factory.%s()" % "Barchart")
            screen_object.name = "barchart"
            manager.add_widget(screen_object)


        self.root.ids.navdrawer.set_state("close")
        self.show_screen()

    def show_screen(self, ):
        self.root.ids.screen_manager.current = "barchart"
        return True


DemoApp().run()
