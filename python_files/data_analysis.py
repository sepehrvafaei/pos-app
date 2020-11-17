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
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("module://kivy.garden.matplotlib.backend_kivy")
from kivy.garden.matplotlib import FigureCanvasKivyAgg


class DataWindow(Screen):
    def show(self):
        if self.ids.entry.text==None:return
        if len(self.ids.graph.children)!=0:self.ids.graph.clear_widgets()
        con=sqlite3.connect('pos_database.db')
        df = pd.read_sql_query("SELECT productData.productID, quantity from salesData INNER JOIN productData ON \
                                productData.productID=salesData.productID", con)
        df=df.groupby('ProductID',as_index=False).sum()
        df=df.sort_values(by='quantity',ascending=False)
        df=df.head(int(self.ids.entry.text))
        df=df.astype({'ProductID':'str'})
        plt.bar(df['ProductID'],df['quantity'])
        plt.xlabel('products')
        plt.ylabel('sales count')
        plt.title('10 most saled products')
        self.ids.graph.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        
        
        
        

