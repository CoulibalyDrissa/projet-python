from tkinter import*
from PIL import ImageTk, Image
from tkinter import ttk,Entry
import  customtkinter
from subprocess import call
fenetre=Tk()
fenetre.title("AW KA HOTEL")
fenetre.geometry("1080x720")
fenetre.config(background='#D9D9D9')
can= Canvas(fenetre,width=1920,height=1080)
img=PhotoImage(file="Chambre (3).png")
can.create_image(690,300,image=img)
can.place(x=0,y=0)

lbltitre = customtkinter.CTkLabel(master=fenetre,text="CHAMBRE",height=30,width=40,border=1,corner_radius=20,bg_color="#FCFAFA",)
lbltitre.place(x=400, y=0, width=200)
lbltitre.pack()

lblnum_chambre = Label(fenetre, text="Num_Chambre", font=("sans serif", 14), background='#60554F', foreground='black')
lblnum_chambre.place(x=10, y=130, width=150)


txtnum_chambre=customtkinter.CTkEntry(master=fenetre,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtnum_chambre.place(x=200,y=130,width=160)


lblcategorie = Label(fenetre, text="Cathegorie_Chambre", font=("sans serif", 14), background='#60554F', foreground='black')
lblcategorie.place(x=5, y=190, width=200)

txtcategorie=customtkinter.CTkEntry(master=fenetre,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
txtcategorie.place(x=200,y=190,width=160)

buttrechercher= customtkinter.CTkButton(master=fenetre,text="Rechercher",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttrechercher.place(x=10,y=510,width=110)

texteRechercher=customtkinter.CTkEntry(master=fenetre,height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
texteRechercher.place(x=160,y=510,width=160)

buttReserver= customtkinter.CTkButton(master=fenetre,text="Reservation",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttReserver.place(x=10,y=300,width=150)

buttEnregistrer= customtkinter.CTkButton(master=fenetre,text="Enregistrer",height=30,width=50,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttEnregistrer.place(x=10,y=560,width=100)


buttmodifier= customtkinter.CTkButton(master=fenetre,text="Modifier",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttmodifier.place(x=150,y=560,width=100)


buttonsupp= customtkinter.CTkButton(master=fenetre,text="Supprimer",height=30,width=40,border_width=1,corner_radius=20,fg_color="#FFFFFF")
buttonsupp.place(x=290,y=560,width=100)

def dashboard():
    fenetre.destroy()
    call(["python","dasboard.py"]) 
b4 = Button(text='<-',font=("Arial",16),background='#5C4D4D',width=5,command=dashboard)
b4.place(x=0, y=0)


tableAfficher = ttk.Treeview(fenetre, columns=(1, 2), height=10, show="headings")
tableAfficher.place(x=730, y=130, width=600, height=600)
style = ttk.Style(fenetre )
style.configure("Treeview",background="#4B8589")
# Entete
tableAfficher.heading(1, text="NumChambre")
tableAfficher.heading(2, text="Catégorie")

# definir les dimentions des colonnes
tableAfficher.column(1, width=10)
tableAfficher.column(2, width=40)


liste = ["a","b"]
tableAfficher.insert('',1,values=liste)
fenetre.state('zoomed')
fenetre.mainloop()
