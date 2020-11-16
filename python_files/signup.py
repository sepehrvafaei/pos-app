from kivy.uix.screenmanager import Screen
import password
class SignupWindow(Screen):
    def change_password(self):
        if self.ids.old_password==password.password:
            password.password=self.ids.password
