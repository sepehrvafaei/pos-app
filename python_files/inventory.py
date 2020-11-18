import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.uix.scrollview import ScrollView
from kivy.uix.recycleview import RecycleView
from kivy.properties import ObjectProperty,NumericProperty
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
import sqlite3
from datetime import datetime
import sys
import database_code


class InventoryWindow(Screen):
    p_ID=ObjectProperty(None)
    name_=ObjectProperty(None)
    brand=ObjectProperty(None)
    qty=ObjectProperty(None)
    u_value=ObjectProperty(None)
    s_ID=ObjectProperty(None)
    def __init__(self):
        super().__init__()
        self.show_all_p()
        self.show_all_s()
        
    def add_product(self):
        entities=(int(self.p_ID.text),self.name_.text,self.brand.text,
                  float(self.u_value.text),int(self.qty.text),
                  (float(self.u_value.text)*int(self.qty.text)),int(self.s_ID.text))
        if None in entities:return
        database_code.addProduct(entities)
        b=BoxLayout(size_hint=(1,None),height=30)
        for col in entities:
                l=Button(text=str(col))
                b.add_widget(l)
        self.ids.product_table.add_widget(b)
        
    def delete_product(self):
        database_code.removeProduct(int(self.p_ID.text))
        for row in self.ids.product_table.children:
            if row.children[6].text==self.p_ID.text:
                self.ids.product_table.remove_widget(row)
        
    def show_product(self):
        con=sqlite3.connect('pos_database.db')
        curObj=con.cursor()
        curObj.execute("SELECT * FROM productData WHERE productID=?",(int(self.p_ID.text),))
        rows=curObj.fetchall()
        con.close()
        if len(rows)>0:
            col=rows[0][::-1]
            for i in range(7):
                self.ids.product_alone.children[i].text=str(col[i])
        
    def show_all_p(self):
        con=sqlite3.connect('pos_database.db')
        curObj=con.cursor()
        curObj.execute("SELECT * FROM productData")
        rows=curObj.fetchall()
        con.close()
        self.ids.product_scroll.add_widget(Label(size_hint=(1,None),height=300))
        for row in rows:
            b=BoxLayout(size_hint=(1,None),height=30)
            for col in row:
                l=Button(text=str(col))
                b.add_widget(l)
            self.ids.product_table.add_widget(b)
    
    def update_product(self):
        entities=(self.name_.text,self.brand.text,
                  float(self.u_value.text),int(self.qty.text),
                  (float(self.u_value.text)*int(self.qty.text)),
                  int(self.s_ID.text),int(self.p_ID.text))
        database_code.updateProduct(entities)
        entities=(int(self.p_ID.text),self.name_.text,self.brand.text,
                  float(self.u_value.text),int(self.qty.text),
                  (float(self.u_value.text)*int(self.qty.text)),
                  int(self.s_ID.text))
        entities=entities[::-1]
        for row in self.ids.product_table.children:
            if row.children[6].text==self.p_ID.text:
                for i in range(6):
                    row.children[i].text=str(entities[i])
    
    def refresh(self):
        con=sqlite3.connect('pos_database.db')
        curObj=con.cursor()
        curObj.execute("SELECT * FROM productData")
        rows=curObj.fetchall()
        con.close()
        self.ids.product_table.clear_widgets()
        for row in rows:
            b=BoxLayout(size_hint=(1,None),height=30)
            for col in row:
                l=Button(text=str(col))
                b.add_widget(l)
            self.ids.product_table.add_widget(b)

    def add_supplier(self):
        entities=(None,self.ids.sup_name.text,self.ids.sup_address.text)
        if None in entities[1:]:return
        id=database_code.addSupplier(entities)
        b=BoxLayout(size_hint=(1,None),height=40)
        for col in entities:
                l=Button(text=str(col),text_size=(300,None),halign='center',valign='center')
                b.add_widget(l)
        b.children[2].text=str(id)
        self.ids.supplier_table.add_widget(b)
        
    def remove_supplier(self):
        database_code.removeSupplier(int(self.s_ID.text))
        for row in self.ids.supplier_table.children:
            if row.children[2].text==self.s_ID.text:
                self.ids.supplier_table.remove_widget(row)
    
    def show_all_s(self):
        con=sqlite3.connect('pos_database.db')
        curObj=con.cursor()
        curObj.execute("SELECT * FROM supplierData")
        rows=curObj.fetchall()
        con.close()
        for row in rows:
            b=BoxLayout(size_hint=(1,None),height=40)
            for col in row:
                l=Button(text=str(col),text_size=(300,None),halign='center',valign='center')
                b.add_widget(l)
            self.ids.supplier_table.add_widget(b)
        
    def update_supplier(self):
        entities=(self.ids.sup_name.text,self.ids.sup_address.text,self.ids.sup_ID)
        database_code.updateSupplier(entities)
