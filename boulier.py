import tkinter as tk

############################
# Définition des constantes

# hauteur du canevas
HAUTEUR = 600
# largeur du canevas
LARGEUR = 600
# nombre de colonnes
N = 9


#######################
# programme principal

# définition des widgets
racine = tk.Tk()
racine.title("Soroban japonais")
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR)

# Créer un ligne horizontal au quart de la hauteur de la fenêtre
canvas.create_line(0, HAUTEUR / 4, LARGEUR, HAUTEUR / 4, fill="darkgrey", width=5)

    # Créer N ligne verticales
for i in range(N):
    canvas.create_line(LARGEUR / (N + 1) * (i + 1), 0, LARGEUR / (N + 1) * (i + 1), HAUTEUR, fill="darkgrey", width=2)

    # Créer des points blancs entre les lignes verticales
for i in range(3, N, 3):
    canvas.create_oval(LARGEUR / (N + 1) * (N - i + 0.5) - 5, HAUTEUR / 4 - 5, LARGEUR / (N + 1) * (N - i + 0.5) + 5, HAUTEUR / 4 + 5, fill="white")

# Créer les boules, 1 au dessus de la ligne horizontale, 4 en dessous
    for i in range(N):
        for j in range(5):
            if j == 0:
                canvas.create_oval(
                    LARGEUR / (N + 1) * (N - i) - 30,
                    HAUTEUR / 8 - HAUTEUR / 16 - 10,
                    LARGEUR / (N + 1) * (N - i) + 30,
                    HAUTEUR / 8 - HAUTEUR / 16 + 30,
                    fill="sienna4"
                )
            else:
                canvas.create_oval(
                    LARGEUR / (N + 1) * (N - i) - 30,
                    HAUTEUR / 4 + ((j + 1) * HAUTEUR / 8) - 10,
                    LARGEUR / (N + 1) * (N - i) + 30,
                    HAUTEUR / 4 + ((j + 1) * HAUTEUR / 8) + 30,
                    fill="sienna4"
                )
canvas.grid()
racine.mainloop()
