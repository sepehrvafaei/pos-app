from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
import database_code
import sqlite3
import password


class SigninWindow(Screen):
    
    def validate(self):
        if self.ids.pwd.text==password.password:
            self.manager.current="home"
        else:
            self.ids.info.text="Invalid username or password."
            

