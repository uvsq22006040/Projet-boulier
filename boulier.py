import tkinter as tk

############################
# Définition des constantes

# hauteur du canevas
HAUTEUR = 600
# largeur du canevas
LARGEUR = 600
# nombre de colonnes
N = int(input("Nombre de colonnes ?"))

#######################
# programme principal

# définition des widgets
racine = tk.Tk()
racine.title("Soroban japonais")
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR)


canvas.mainloop
