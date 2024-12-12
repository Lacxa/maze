from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.clock import mainthread
from auth_google import login_with_google
import threading


class LoginScreen(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Google Login Button
        self.google_button = MDRaisedButton(
            text="Login with Google",
            pos_hint={"center_x": 0.5},
            on_release=self.start_google_login
        )
        self.add_widget(self.google_button)

        # Status Label
        self.status_label = MDLabel(
            text="Not logged in",
            halign="center",
            theme_text_color="Hint"
        )
        self.add_widget(self.status_label)

    def start_google_login(self, instance):
        # Start Google login in a thread
        threading.Thread(target=self.google_login_thread).start()

    def google_login_thread(self):
        try:
            user_info = login_with_google()
            self.update_status(f"Logged in as {user_info.get('name')}")
        except Exception as e:
            self.update_status(f"Login failed: {str(e)}")

    @mainthread
    def update_status(self, message):
        self.status_label.text = message


class GoogleLoginApp(MDApp):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    GoogleLoginApp().run()
