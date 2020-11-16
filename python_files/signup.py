from kivy.uix.screenmanager import Screen

class SignupWindow(Screen):
    def change_password(self):
        with open('password.txt','r') as r:
            data=r.read()
        if self.ids.old_password.text==data:
            with open('password.txt','w') as w:
                w.write(self.ids.password.text)