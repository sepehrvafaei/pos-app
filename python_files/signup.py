from kivy.uix.screenmanager import Screen
import json
class SignupWindow(Screen):
    def change_password(self):
        r=open('password.json','r')
        data=json.load(r)
        r.close()
        if self.ids.old_password==data['password']:
            data['password']=self.ids.password
            w=open('password.json','w')
            json.dump(data,w)
            w.close()
