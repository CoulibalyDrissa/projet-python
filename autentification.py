from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import  customtkinter
from subprocess import call
import pymysql
fenetre = Tk()
fenetre.title("AW KA HÔTEL")
fenetre.geometry("800x700")
imag=ImageTk.PhotoImage(Image.open("images (5).png"))
x=Label(image=imag,font=("Arial",30))
x.pack()
a=Frame(fenetre,width=800,height=400,bg="#4B8589")

s=Label(a,text="CONNEXION", font=("Arial", 20), width=38, height=1, fg="#FFFFFF",bg="#4B8589")
s.place(x=120,y=20)



email = Label(a, text="EMAIL ", font=("Arial", 20), width=6, height=1,  fg="#FFFFFF",bg="#4B8589")
#Nom.grid(row=0, column=0)
email.place(x=1,y=100)

#entre1= Entry(a, font=("Arial", 20), bg="#9E9696", fg="black", width=20)
#entre1.place(x=300,y=110)
v1=StringVar()
entre1=customtkinter.CTkEntry(master=fenetre,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF",textvariable=v1)
entre1.place(x=550,y=300, width=300)

mot_passe=Label(a, text="MOT DE PASSE ", font=("Arial", 20), width=13, height=2,  fg="#FFFFFF",bg="#4B8589")
mot_passe.place(x=4,y=150 )
v2=StringVar()
entre2=customtkinter.CTkEntry(master=fenetre,textvariable=v2, height=30,width=40,bg= "#4B8589",border_width=1,corner_radius=20,fg_color="#FFFFFF")
entre2.place(x=550,y=370, width=300)

#entre2= Entry(a, font=("Arial", 20), bg="#9E9696", fg="black", width=20)
#entre2.place(x=300,y=170)

def connecter():
    mdp=entre2.get()
    nb=mdp.count(__start=0,__end=END)
    if entre1.get()=="" or entre2.get()=="":
        messagebox.showinfo("Echec","Tous les sont réquis")
    elif nb>8:
        messagebox.showinfo("Echec","le nombre de caractère mot de passe ne doit pas dépassé 8")
    else:
     fenetre.destroy()
     call(["python","dasboard.py"])

#bouton=#Button=Button(a,text="se connecter",font=("Arial", 15), width=17, height=1,  fg="white",bg="#5C4D4D")
#bouton.#place(x=200,y=300)
button= customtkinter.CTkButton(master=fenetre,text="se connecter",height=30,width=40,border_width=2,corner_radius=20,fg_color="#FFFFFF",command=connecter)
button.place(x=650,y=450)
#b4 = Button(text='<-',font=("Arial",16),background='#5C4D4D',width=5)
#b4.place(x=0, y=0)


a.pack_propagate(False)
a.pack(expand=YES)
a.pack()
a.place(x=260,y=200)
fenetre.state('zoomed')




fenetre.mainloop()
