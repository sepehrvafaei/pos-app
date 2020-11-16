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

    def add_costumer(self):
        entities=(None,self.ids.name_f.text,self.ids.name_l.text,
                  self.ids.email.text,self.ids.phone.text,self.ids.city.text)
        database_code.addCostumer(entities)
        if len(self.costumer_table.children)==0:return
        self.costumer_table.height+=40
        b=BoxLayout(size_hint=(None,None),height=40,width=1200)
        for col in entities:
            l=Button(text=str(col),text_size=(120,None),halign='center',valign='center')
            b.add_widget(l)
        self.costumer_table.add_widget(b)

    def delete_costumer(self):
        database_code.removeCostumer(int(self.ids.clientID.text))
        if self.ids.clientID.text!=None:
            for row in self.ids.costumer_table.children:
                if row.children[5].text==int(self.ids.clientID.text):
                    self.ids.costumer_table.remove_widget(row)
        else:return

    def show_costumer(self):
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
            self.ids.costumer_table.add_widget(b)
        self.ids.options.children[4].disabled=True
    
    def update_costumer(self):
        entities=(self.ids.name_f.text,self.ids.name_l.text,
                  self.ids.email.text,self.ids.phone.text,
                  self.ids.city.text,int(self.ids.clientID.text))
        database_code.updateCostumer(entities)
        if len(self.ids.costumer_table.children)==0:return
        entities=(self.ids.clientID,self.ids.name_f.text,
                self.ids.name_l.text,self.ids.email.text,
                self.ids.phone.text,self.ids.city.text)
        if self.ids.clientID.text!=None:
            for row in self.ids.costumer_table.children:
                if row.children[5].text==int(self.ids.clientID.text):
                    for i in range(6):
                        row.children[i]=entities[i-6]
        else:return
