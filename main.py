import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.uix.scrollview import ScrollView
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
import database_code
import sqlite3
from datetime import datetime
from python_files import signin
from python_files import signup
from python_files import home
from python_files import payment
from python_files import sales
from python_files import costumer
from python_files import inventory
from python_files import staff
from python_files import data_analysis


Builder.load_file("kv_files/signin.kv")
Builder.load_file("kv_files/signup.kv")
Builder.load_file("kv_files/home.kv")
Builder.load_file("kv_files/costumer.kv")
Builder.load_file("kv_files/staff.kv")
Builder.load_file("kv_files/payment.kv")
Builder.load_file("kv_files/sales.kv")
Builder.load_file("kv_files/inventory.kv")
Builder.load_file("kv_files/data_analysis.kv")

SM=ScreenManager()
SM.add_widget(signin.SigninWindow())
SM.add_widget(signup.SignupWindow())
SM.add_widget(home.HomeWindow())
SM.add_widget(costumer.CostumerWindow())
SM.add_widget(staff.StaffWindow())
SM.add_widget(payment.PaymentWindow())
SM.add_widget(sales.SalesWindow())
SM.add_widget(inventory.InventoryWindow())
SM.add_widget(data_analysis.DataWindow())

class MainApp(App):
    def build(self):
        return SM

if __name__ == "__main__":
    MainApp().run()
