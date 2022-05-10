
import tkinter as tk
import time

C = 9

HAUTEUR = 600

LARGEUR = 100 * C
GAPX = 100
GAPY = 80

def init():
    
    canvas.create_rectangle(10, 10, LARGEUR , HAUTEUR, width=10)
    canvas.create_line(10, 150, LARGEUR, 150, width=10)
    
    for j in range(4):
        for i in range(C):
            canvas.create_line(47+GAPX*i,10,47+GAPX*i,HAUTEUR, width=5)
            canvas.create_oval(20+GAPX*i,200+GAPY*j,75+GAPX*i,255+GAPY*j, fill="black")
        

    for i in range(C):
        canvas.create_oval(20+GAPX*i,20,75+GAPX*i,75, fill="black")

def clic(event):
    bille = canvas.find_closest(event.x,event.y,"oval")
    billetags = canvas.gettags(bille)
    colonnebille = int(billetags[1])
    pass


racine = tk.Tk()
racine.title("boulier")
canvas = tk.Canvas(racine, height = HAUTEUR, width = LARGEUR, bg="white")
canvas.grid()

canvas.create_rectangle(10, 10, LARGEUR , HAUTEUR, width=10)
canvas.create_line(10, 150, LARGEUR, 150, width=10)



init()


racine.mainloop()
