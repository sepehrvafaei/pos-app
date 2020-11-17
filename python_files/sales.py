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

class SalesWindow(Screen):
    def __init__(self):
        super().__init__()
        self.show_all()
    
    def show_all(self):
        con=sqlite3.connect('pos_database.db')
        curObj=con.cursor()
        curObj.execute("SELECT * FROM salesData")
        con.commit()
        rows=curObj.fetchall()
        con.close()
        if len(rows)==0:return
        for row in rows:
            b=BoxLayout(size_hint=(None,None),height=30,width=1000)
            for col in row:
                l=Button(text=str(col))
                b.add_widget(l)
            self.ids.sales_table.add_widget(b)

    def show_sale(self):
        con=sqlite3.connect('pos_database.db')
        curObj=con.cursor()
        curObj.execute("SELECT * FROM salesData WHERE saleID=?",(int(self.ids.entry.text),))
        con.commit()
        rows=curObj.fetchall()
        con.close()
        sale=rows[0][::-1]
        if len(rows)==0:return
        i=0
        for col in self.ids.sale_alone.children:
            col.text=str(sale[i])
            i+=1
            

