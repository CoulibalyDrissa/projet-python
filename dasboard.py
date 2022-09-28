
from tkinter import *
import tkinter.ttk as ttk
from turtle import width
from PIL import ImageTk, Image
import os
import datetime
from subprocess import call
from tkinter import ttk,Entry
import customtkinter



fenetre=Tk()
fenetre.title("Hotel")
fenetre.geometry("1280x720")
fenetre.minsize(480,320)
fenetre.config(background='#D9D9D9')
#fenetre.attributes('-alpha',0.7)
#fenetre.iconbitmap("IKA_HOTEL.ico")

can=Canvas(fenetre,width=1280,height=740)
img=PhotoImage(file="image_back2.png")
can.create_image(637,350,image=img)
can.place(x=0,y=0)
photo1 = PhotoImage(file = "employe.png") 
photo2 = PhotoImage(file = "chambre (4).png")
photo3 = PhotoImage(file = "client.png")
photo4 = PhotoImage(file = "salle.png")
photo5 = PhotoImage(file = "restaurant.png")

def employer():
    fenetre.destroy()
    call(["python","Employe.py"])

def chambre():
    fenetre.destroy()
    call(["python","chambre.py"])
    
def client():
    fenetre.destroy()
    call(["python","Client.py"])
    
def salle():
    fenetre.destroy()
    call(["python","Salle.py"])
    
def restaurant():
    fenetre.destroy()
    call(["python","Restaurant.py"])
#cadre=Frame(fenetre,bg='#C6C2C2',bd=1,relief=SUNKEN,height=515,width=350)
#cadre.place(x=250,y=200)

# Ajouter l'image dans le bouton 
#Button(gui, image=photo).pack(side=TOP) 
"""def slide(x):
    fenetre.attributes('-alpha',my_slider.get())
    


my_slider=ttk.Scale(cadre,from_=0.1,to=1.0,value=0.7,orient=HORIZONTAL,command=slide)
my_slider.pack(pady=60)."""



#b1 =Button(fenetre,image=photo1, text="",background='#FFFFFF',font=("Inria Sans",30),fg="#000000",width=153).place(x=0,y=1)

b1= customtkinter.CTkButton(master=fenetre,hover_color="#F4F4F4",image=photo1,text="",height=30,width=153,border_width=1,corner_radius=20,fg_color="#ffffff",command=employer).place(x=0,y=1,width=153)
#buttEnregistrer.place(x=10,y=560,width=100)
b2 =customtkinter.CTkButton(master=fenetre,hover_color="#F4F4F4",image=photo2, text="",fg_color="#ffffff",border_width=1,corner_radius=20,width=153,command=chambre).place(x=270,y=1)

b3 =customtkinter.CTkButton(master=fenetre,hover_color="#F4F4F4",image=photo3, text="",fg_color="#ffffff",border_width=1,corner_radius=20,width=153,command=client).place(x=550,y=1)

b4=customtkinter.CTkButton(fenetre,image=photo4,hover_color="#F4F4F4", text="",fg_color="#ffffff",border_width=1,corner_radius=20,width=153,command=salle).place(x=830,y=1)

b5 =customtkinter.CTkButton(fenetre,image=photo5,hover_color="#F4F4F4",text="",fg_color="#ffffff",border_width=1,corner_radius=20,width=153,command=restaurant).place(x=1108,y=1)


"""cadre=Frame(fenetre,bg='#C6C2C2',bd=1,relief=SUNKEN,height=515,width=350)

def client():
    fenetre.destroy()
    call(["python","client.py"])

def chambre():
    fenetre.destroy()
    call(["python","chambre.py"])

def employe():
    fenetre.destroy()
    call(["python","empoye.py"])

def salle():
    fenetre.destroy()
    call(["python","salle.py"])

b1 =Button(cadre, text="CLIENT",background='#5C4D4D',font=("Inria Sans",30),fg="#ffffff",width=15,command=client)
b1.place(y=1, x=2)

b2 =Button(cadre, text="CHAMBRE",background='#5C4D4D',font=("Inria Sans",30),fg="#ffffff",width=15,command=chambre)
b2.place(y=150, x=2)

b3 =Button(cadre, text="SALLE",background='#5C4D4D',font=("Inria Sans",30),fg="#ffffff",width=15,command=salle)
b3.place(y=290, x=2)

b4 =Button(cadre, text="EMPLOYE",background='#5C4D4D',font=("Inria Sans",30),fg="#ffffff",width=15,command=employe)
b4.place(y=430, x=2)

cadre1=Frame(fenetre,bg='#C6C2C2',bd=1,relief=SUNKEN,height=200,width=300)
nom=Label(cadre1,text="!!!!!!",font=('Inria Sans',50),bg='#A69D9D').pack(expand=YES)
cadre1.pack_propagate(False)
cadre1.place(x=430,y=185)

cadre2=Frame(fenetre,bg='#C6C2C2',bd=1,relief=SUNKEN,height=200,width=300)
nom=Label(cadre2,text="!!!!!!",font=('Inria Sans',50),bg='#A69D9D').pack(expand=YES)
cadre2.pack_propagate(False)
cadre2.place(x=900,y=185)

cadre3=Frame(fenetre,bg='#C6C2C2',bd=1,relief=SUNKEN,height=200,width=300)
nom=Label(cadre3,text="!!!!!!",font=('Inria Sans',50),bg='#A69D9D').pack(expand=YES)
cadre3.pack_propagate(False)
cadre3.place(x=430,y=490)

cadre4=Frame(fenetre,bg='#C6C2C2',bd=1,relief=SUNKEN,height=200,width=300)
nom=Label(cadre4,text="!!!!!!",font=('Inria Sans',50),bg='#A69D9D').pack(expand=YES)
cadre4.pack_propagate(False)
cadre4.place(x=900,y=490)

cadre5=Frame(fenetre,bg='#5C4D4D',bd=1,relief=SUNKEN,height=175,width=900)
img = ImageTk.PhotoImage(Image.open("IKA_HOTEL.ico"),size=1)
panel =Label(cadre5, image = img,width=600)
panel.pack(side = "left")


date = datetime.date.today()
print(date)
panel1 =Label(cadre5, text=date,width=425,bg='#5C4D4D',font=("Inria Sans",20),fg="#ffffff")
panel1.pack(side = "right")

cadre5.pack_propagate(False)
cadre5.place(x=1,y=1)


degiskenler=['CLIENT','CHAMBRE','SALLE','EMPLOYE']
rolechamp=Combobox(fenetre, values=degiskenler,font=("Inria Sans",20)).place(width=200,height=40,y=130,x=1000)

nom=Label(fenetre,text="Email:neka_hotel@gmail.com     Contact:+223 71195096     Adresse:ACI 2000",font=('Inria Sans',10),bg='#A69D9D').pack(side=BOTTOM)

cadre.pack_propagate(False)
cadre.place(x=1,y=180)."""

fenetre.state("zoomed")
fenetre.mainloop()