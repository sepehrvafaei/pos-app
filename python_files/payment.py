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

class PaymentWindow(Screen):
    def __init__(self):
        super().__init__()
        self.items={}

    def add_row(self):
        con=sqlite3.connect('pos_database.db')
        curObj=con.cursor()
        curObj.execute("SELECT * FROM productData WHERE productID=?",(int(self.ids.product_id.text),))
        con.commit()
        rows=curObj.fetchall()
        con.close()
        if int(self.ids.product_id.text) not in self.items.keys():
            self.items[int(self.ids.product_id.text)]=[
                None, int(self.ids.product_id.text), 1,
                rows[0][3],
                int(self.ids.staff_id.text),
                int(self.ids.costumer_id.text),datetime.now().strftime("%Y-%m-%d %X")
                ]
        else:
            self.items[int(self.ids.product_id.text)][2]+=1
            self.items[int(self.ids.product_id.text)][3]+=rows[0][3]
        b=BoxLayout(size_hint=(1,None),height=40)
        L1=Button(text=str(rows[0][1]))
        L2=Button(text=str(rows[0][2]))
        L3=Button(text=str(rows[0][3]))
        b.add_widget(L1)
        b.add_widget(L2)
        b.add_widget(L3)
        self.ids.pay_table.add_widget(b)
        new_subtotal=str(float(self.ids.subtotal.text)+rows[0][3])
        self.ids.subtotal.text=new_subtotal
        self.ids.total.text=str((float(self.ids.subtotal.text)*(1-float(self.ids.discount.text)))*(1+float(self.ids.tax.text)))
    
    def confirm(self):
        for key in self.items.keys():
            database_code.updateProductQ((self.items[key][2], self.items[key][3], self.items[key][1]))
            id=database_code.addSales(self.items[key])
            self.items[key][0]=id
        self.cancel()
    
    def cancel(self):
        self.ids.pay_table.clear_widgets()
        self.ids.subtotal.text=''
        self.ids.total.text=''
        self.ids.discount.text=''