from tkinter import *
from tkinter import messagebox
from tkinter import ttk,Entry
import  customtkinter

root = Tk()
root.title("Aw KA HOTEL")
root.geometry("1000x650")
root.resizable(False, False)
root.configure(background='#60554F')

lbltitre = customtkinter.CTkLabel(master=root,text="Salle",height=30,width=40,border=1,corner_radius=20,bg_color="#FCFAFA",)
lbltitre.place(x=400, y=0, width=200)

lblnom = Label(root, text="Num_Salle", font=("sans serif", 14), background='#60554F', foreground='black')
lblnom.place(x=10, y=130, width=150)
txtdate=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtdate.place(x=200,y=130,width=160)
lblprenom = Label(root, text="Cathegorie_Salle", font=("sans serif", 14), background='#60554F', foreground='black')
lblprenom.place(x=5, y=190, width=200)
txtdate=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtdate.place(x=200,y=190,width=160)

buttrechercher= customtkinter.CTkButton(master=root,text="Rechercher",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttrechercher.place(x=10,y=300,width=110)
txtrechercher=customtkinter.CTkEntry(master=root,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtrechercher.place(x=200,y=300,width=160)

buttmodifier= customtkinter.CTkButton(master=root,text="Reservation",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttmodifier.place(x=10,y=450,width=150)


buttEnregistrer= customtkinter.CTkButton(master=root,text="Enregistrer",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttEnregistrer.place(x=10,y=560,width=100)


buttmodifier= customtkinter.CTkButton(master=root,text="Modifier",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttmodifier.place(x=115,y=560,width=100)


buttonsupp= customtkinter.CTkButton(master=root,text="Supprimer",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttonsupp.place(x=220,y=560,width=100)

tableAfficher = ttk.Treeview(root, columns=(1, 2), height=10, show="headings")
tableAfficher.place(x=400, y=130, width=600, height=600)
style = ttk.Style(root)
style.configure("Treeview",background="#D9D9D9")
# Entete
tableAfficher.heading(1, text="Num_Salle")
tableAfficher.heading(2, text="Categorie")

# definir les dimentions des colonnes
tableAfficher.column(1, width=100)
tableAfficher.column(2, width=100)

liste = ["a","b"]
tableAfficher.insert('',1,values=liste)

root.mainloop()