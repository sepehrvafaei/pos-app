from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
import database_code
import sqlite3

class SigninWindow(Screen):
    
    def validate(self):
        r=open('password.txt','r')
        data=r.read()
        r.close()
        if self.ids.pwd.text==data:
            self.manager.current="home"
        else:
            self.ids.info.text="Invalid password."
            

