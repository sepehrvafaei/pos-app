from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
import database_code
import sqlite3
import json


class SigninWindow(Screen):
    
    def validate(self):
        with open('password.json') as f:
            data=json.load(f)
        if self.ids.pwd.text==data['password']:
            self.manager.current="home"
        else:
            self.ids.info.text="Invalid password."
            

