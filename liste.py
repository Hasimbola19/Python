from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror, showinfo

# from listedesinscrit import listeInscrit

listePersonne = []


class Personnage:
    def __init__(self, prenom, nom, numero, adresse, photo):
        self.prenom = prenom
        self.nom = nom
        self.numero = numero
        self.adresse = adresse
        self.photo = photo

    def __eq__(self, other):
        return (self.prenom == other.prenom and self.nom == other.nom and self.numero == other.numero)

    def parcourir(self):
        global imageName
        imn = askopenfilename(initialdir="/", title="Selectionner une image",
                              filetypes=(("png files", "*.png"), ("JPG files", "*.jpg")))
        if imn:
            imageName = imn
        if imageName:
            texte = imageName.split("/")
            photoEntre.configure(text=".../" + texte[-1])

    def appartient(self, liste, val):
        for i in range(len(liste)):
            if liste[i].__eq__(val):
                return TRUE
            return FALSE

    def valider(self):
        global imageName
        photo = imageName
        if prenomEntre.get() and nomEntre.get() and numeroEntre.get() and adresseEntre.get() and photo:
            pn = Personnage(prenomEntre.get(), nomEntre.get(), numeroEntre.get(), adresseEntre.get(), photo)
            if self.appartient(self, liste=listePersonne, val=pn):
                showerror(title="Erreur", message="Déja ajouté !")
            else:
                listePersonne.append(pn)
                showinfo(title="Ajout réussi", message="{} a bien été ajouter".format(pn.prenom))
        else:
            showerror(title="Erreur", message="Vous devez remplir tous les champs !")

    def reinitialiser(self):
        global imageName
        prenomEntre.delete(0, END)
        nomEntre.delete(0, END)
        numeroEntre.delete(0, END)
        adresseEntre.delete(0, END)
        imageName = ''
        photoEntre.configure(text="Aucune image selectionnée")

    imageName, listePersonne = '', []


Personnage

fen = Tk()
fen.geometry("320x380")
fen.title("Page d'inscription")

contenu = Canvas(fen, bg="#0005FF")

fontLabel = "arial 13 bold"
fontEntre = "arial 11 bold"

prenom = Label(contenu, text="votre prenom : ", font=fontLabel, fg="white", bg="#0005FF")
nom = Label(contenu, text="votre nom : ", font=fontLabel, fg="white", bg="#0005FF")
numero = Label(contenu, text="votre numero : ", font=fontLabel, fg="white", bg="#0005FF")
adresse = Label(contenu, text="votre adresse : ", font=fontLabel, fg="white", bg="#0005FF")
photo = Label(contenu, text="votre photo : ", font=fontLabel, fg="white", bg="#0005FF")
validation = Label(contenu, text="Entrez vos informations : ", font=fontLabel, fg="#0005FF", bg="white")

prenomEntre = Entry(contenu, font=fontEntre)
nomEntre = Entry(contenu, font=fontEntre)
numeroEntre = Entry(contenu, font=fontEntre)
adresseEntre = Entry(contenu, font=fontEntre)
photoEntre = Label(contenu, text="Aucune image selectionnee ", font="arial 8 bold", fg="#0005FF", bg="#0088FF")
bouttonParcourir = Button(contenu, text="...", command=lambda: Personnage.parcourir(Personnage), fg="#0005FF",
                          bg="white")

validation.grid(row=0, column=0, columnspan=2)
prenom.grid(row=1, column=0, sticky=E, padx=5, pady=5)
nom.grid(row=2, column=0, sticky=E, padx=5, pady=5)
numero.grid(row=3, column=0, sticky=E, padx=5, pady=5)
adresse.grid(row=4, column=0, sticky=E, padx=5, pady=5)
photo.grid(row=5, column=0, sticky=E, padx=5, pady=5)

prenomEntre.grid(row=1, column=1, padx=5, pady=5)
nomEntre.grid(row=2, column=1, padx=5, pady=5)
numeroEntre.grid(row=3, column=1, padx=5, pady=5)
adresseEntre.grid(row=4, column=1, padx=5, pady=5)
photoEntre.grid(row=5, column=1, padx=5, pady=5, sticky=W)
bouttonParcourir.grid(row=6, column=1, padx=5, pady=5, sticky=E)

listePersonne = []
boutton1 = Button(fen, text="Valider", command=lambda: Personnage.valider(Personnage), width=10, fg="white",
                  bg="#0005FF")
boutton2 = Button(fen, text="Reinitialiser", command=lambda: Personnage.reinitialiser(Personnage), width=10, fg="white",
                  bg="#0005FF")
boutton3 = Button(fen, text="Afficher", command="", width=10, fg="white", bg="#0005FF")

boutton1.grid(row=7, column=0, pady=5)
boutton2.grid(row=8, column=0, pady=5)
boutton3.grid(row=9, column=0, pady=5)

contenu.grid(row=0, column=0, padx=5, pady=5)
fen.mainloop()
