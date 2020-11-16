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
class CostumerWindow(Screen):
    costumer_table=ObjectProperty(None)
    def add_customer(self):
        entities=(None,self.ids.name_f.text,self.ids.name_l.text,
                  self.ids.email.text,self.ids.phone.text,self.ids.city.text)
        database_code.addCostumer(entities)
        self.costumer_table.height+=40
        b=BoxLayout(size_hint=(None,None),height=40,width=1200)
        for col in entities:
            l=Button(text=str(col),text_size=(120,None),halign='center',valign='center')
            b.add_widget(l)
        self.costumer_table.add_widget(b)

    def delete_customer(self):
        database_code.removeCostumer(self.ids.email.text)

    def show_customer(self):
        con=sqlite3.connect('pos_database.db')
        curObj=con.cursor()
        curObj.execute("SELECT * FROM costumerData WHERE email=?",(self.ids.email.text,))
        rows=curObj.fetchall()
        con.close()
        if len(rows)>0:
            cols=rows[0][::-1]
            for i in range(6):
                self.ids.costumer_alone.children[i].text=str(cols[i])

    def show_all(self):
        con=sqlite3.connect('pos_database.db')
        curObj=con.cursor()
        curObj.execute("SELECT * FROM costumerData")
        rows=curObj.fetchall()
        con.close()
        if len(rows)==0:return
        for row in rows:
            b=BoxLayout(size_hint=(None,None),height=40,width=1200)
            for col in row:
                l=Button(text=str(col),text_size=(120,None),halign='center',valign='center')
                b.add_widget(l)
            self.costumer_table.add_widget(b)
        self.ids.options.children[4].disabled=False
