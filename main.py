# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:19:05 2020

@author: tyagid
"""


from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy,os
from cv2 import *
import cv2
import time
from pandas import *



def upload_image():
    string=searchText.get()
    print(string)
    pass






# Focusing on the Entry field something got written then enable the Button
def stateSearchButton(*_):
   
    
    if(entrySearchBox.searchText.get()):
        searchButton["state"]="normal"
    else:
         searchButton["state"]="disable"

def entryBoxFocus(event):
   
    entrySearchBox.delete(0,"end")
    


#initialise GUI
top=Tk()
top.geometry('1080x720')
top.title('Qt Support App')
top.configure(background='#CDCDCD')


searchButton=Button(top,text="Search",command=upload_image)
searchButton.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
searchButton.place(x=690,y=120,width=100,height=29)
searchButton["state"]="disabled"


searchText=StringVar()




entrySearchBox=Entry(top,textvariable=searchText,font=('Verdana',10), bg = "white")
entrySearchBox.place(x=320,y=120,width=350,height=30)
entrySearchBox.searchText=StringVar(top,value="Search")
entrySearchBox['textvariable']=entrySearchBox.searchText
entrySearchBox.searchText.trace_add('write',stateSearchButton)
entrySearchBox.bind("<Button-1>",entryBoxFocus)
#entrySearchBox.bind("<Button-1>",stateSearchButton)
  


mainLable = Label(top, text="Qt Design Studio Support",pady=20, font=('arial',20,'bold'))
mainLable.configure(background='#CDCDCD',foreground='#364156')
mainLable.place(x=350,y=30)
top.mainloop()
