from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.metrics import dp


class DataEntry(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = dp(10)
        self.spacing = dp(5)

        self.add_widget(MDLabel(text="S/n"))
        self.sn = TextInput(hint_text="S/n", input_type="number", size_hint_y=None, height=dp(40))
        self.add_widget(self.sn)

        self.add_widget(MDLabel(text="Date"))
        self.date = TextInput(hint_text="Date (DD/MM/YYYY)", size_hint_y=None, height=dp(40))
        self.add_widget(self.date)

        self.add_widget(MDLabel(text="Student Name"))
        self.student_name = TextInput(hint_text="Student Name", size_hint_y=None, height=dp(40))
        self.add_widget(self.student_name)

        self.add_widget(MDLabel(text="Grade Level"))
        self.grade_level = TextInput(hint_text="Grade Level", input_type="number", size_hint_y=None, height=dp(40))
        self.add_widget(self.grade_level)

        self.add_widget(MDLabel(text="Age"))
        self.age = TextInput(hint_text="Age", input_type="number", size_hint_y=None, height=dp(40))
        self.add_widget(self.age)

        self.add_widget(MDLabel(text="Activity Name"))
        self.activity_name = TextInput(hint_text="Activity Name", size_hint_y=None, height=dp(40))
        self.add_widget(self.activity_name)

        # ... (Enthusiasm to Knowledge Acquisition - similar structure)

        self.ratings = {}
        for metric in ["Enthusiasm", "Problem-Solving Skills", "Teamwork", "Creativity", "Communication", "Knowledge Acquisition"]:
            self.add_widget(MDLabel(text=metric))
            rating_input = TextInput(hint_text=metric + " (1-5)", input_type="number", size_hint_y=None, height=dp(40))
            self.add_widget(rating_input)
            self.ratings[metric] = rating_input  # Store references to the input fields


    def get_data(self):
        data = {
            "S/n": self.sn.text,
            "Date": self.date.text,
            "Student Name": self.student_name.text,
            "Grade Level": self.grade_level.text,
            "Age": self.age.text,
            "Activity Name": self.activity_name.text,
        }
        for metric, input_field in self.ratings.items():
            data[metric] = input_field.text
        return data


class DataTable(ScrollView):  # Use ScrollView for larger datasets
    data = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid = GridLayout(cols=12, spacing=dp(1), size_hint_y=None) # 12 columns
        self.grid.bind(minimum_size=self.grid.setter('size'))  # Important for ScrollView
        self.add_widget(self.grid)
        self.bind(data=self.update_table) # Update when data changes

    def update_table(self, *args):
        self.grid.clear_widgets()  # Clear existing data

        # Header Row
        headers = ["S/n", "Date", "Student Name", "Grade Level", "Age", "Activity Name", "Enthusiasm", "Problem-Solving Skills", "Teamwork", "Creativity", "Communication", "Knowledge Acquisition"]
        for header in headers:
            self.grid.add_widget(MDLabel(text=header, size_hint_y=None, height=dp(40))) # Consistent height

        # Data Rows
        for row_data in self.data:
            for header in headers:
                value = row_data.get(header, "")  # Handle missing data
                self.grid.add_widget(MDLabel(text=str(value), size_hint_y=None, height=dp(40)))


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical")
        self.add_widget(self.layout)

        self.data_entry = DataEntry()
        self.layout.add_widget(self.data_entry)

        self.data_table = DataTable(size_hint_y=None, height=dp(300)) # Fixed height for the table
        self.layout.add_widget(self.data_table)

        add_button = MDFlatButton(text="Add Data", on_press=self.add_data)
        self.layout.add_widget(add_button)

    def add_data(self, instance):
        data = self.data_entry.get_data()
        self.data_table.data.append(data) # Append to the data list
        self.data_table.data = self.data_table.data # Trigger the update (important!)

        # Clear input fields after adding
        for widget in self.data_entry.children:
            if isinstance(widget, TextInput):
                widget.text = ""


class MyApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen = MainScreen(name="main")
        screen_manager.add_widget(screen)
        return screen_manager


if __name__ == "__main__":
    MyApp().run()