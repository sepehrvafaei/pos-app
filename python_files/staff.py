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

class StaffWindow(Screen):

    def __init__(self):
        super().__init__()
        self.show_all()
    
    def add_staff(self):
        entities=(None,self.ids.name_f.text,self.ids.name_l.text,
                  self.ids.email.text,self.ids.phone.text,self.ids.address.text,
                  self.ids.city.text,self.ids.birth.text,self.ids.gender.text,self.ids.postal.text)
        id=database_code.addStaff(entities)
        b=BoxLayout(size_hint=(None,None),height=40,width=1200)
        for col in entities:
            l=Button(text=str(col),text_size=(120,None),halign='center',valign='center')
            b.add_widget(l)
        b.children[9].text=str(id)
        self.ids.staff_table.add_widget(b)

    def delete_staff(self):
        if self.ids.satffID.text!=None:
            database_code.removeStaff(int(self.ids.staffID.text))
            for row in self.ids.staff_table.children:
                if row.chilren[9].text==int(self.ids.staffID.text):
                    self.ids.staff_table.remove_widget(row)
        else:return

    def update_satff(self):
        entities=(int(self.ids.satffID.text),self.ids.name_f.text,self.ids.name_l.text,
                  self.ids.email.text,self.ids.phone.text,self.ids.address.text,
                  self.ids.city.text,self.ids.birth.text,self.ids.gender.text,self.ids.postal.text)
        L=entities[::-1]
        if self.ids.staffID.text!=None:
            for row in self.ids.staff_table.children:
                if row.chilren[9].text==int(self.ids.staffID.text):
                    for i in range(10):
                        row.children[i]=L[i]
        else:return

    def show_all(self):
        con=sqlite3.connect('pos_database.db')
        curObj=con.cursor()
        curObj.execute("SELECT * FROM staffData")
        rows=curObj.fetchall()
        con.close()
        if len(rows)==0:return
        for row in rows:
            b=BoxLayout(size_hint=(1,None),height=40)
            for col in row:
                l=Button(text=str(col),text_size=(120,None),halign='center',valign='center')
                b.add_widget(l)
            self.ids.staff_table.add_widget(b)

