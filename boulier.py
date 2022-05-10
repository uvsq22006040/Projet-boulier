####################################
# Groupe 8
# MIASHS TD 02
# Michael GREKOBI
# Pierre-Axel RIVIERE
# Jeremy SALEH
# Ilyes MAGHLAOUA
# https://github.com/uvsq22006040/Projet-boulier
####################################


#######################
# import des librairies
import tkinter as tk
import time

############################
#Variables globales en listes
listebille1=[]
listebille2=[]
listebille3=[]
listebille4=[]
listebille5=[]

placementbille1=[]
placementbille2=[]
placementbille3=[]
placementbille4=[]
placementbille5=[]


listechiffre=[]



############################   
#Coordonéés de la vitesse
v=0.01

#Colonnes
n=1


############################
#Operation variables
operande1=0
operande2=0





#######################
# Fonctions


def clic(event):
    """Permet de changer les billes de place selon l'etat de la variable placementbille."""

    global canvas   
    global listebille1,listebille2,listebille3,listebille4,listebille5
    global placementbille1, placementbille2,placementbille3,placementbille4,placementbille5 

    bille = canvas.find_closest(event.x, event.y)
    # permet d'identifier l'objet le plus proche du point où on a cliqué

    billetags = canvas.gettags(bille)
    #liste des tags qu'on va associer à la bille dans la variable billetags


    if (canvas.type(bille) == "oval" and len(billetags) > 1):
        
        
        # on recupere la colonne de la bille : cela permet d'accéder aux variables globales qui disent si elle est activée, et aux autres billes de la colonne si il faut les déplacer aussi
        colonnebille = int(billetags[1])#colonne bille correspond au tag 1
        deplacementdesbilles(colonnebille,billetags[0],bille)

        # gesion de la bille 5


def deplacementdesbilles(colonnebille,numerobille,bille):
    """"""
    global canvas   
    global listebille1,listebille2,listebille3,listebille4,listebille5
    global placementbille1, placementbille2,placementbille3,placementbille4,placementbille5 
    

    
    if (numerobille=="5"):
            
            if (placementbille5[colonnebille]==True):#=Placementbille5 de colonne bille vaut false
                initialise_mouvement(bille,True)
                placementbille5[colonnebille]=False
            else:
                initialise_mouvement(bille,False)

                placementbille5[colonnebille]=True
            

    if (numerobille=="1"):
            if (placementbille1[colonnebille]==True):
                if (placementbille4[colonnebille]==True):
                    initialise_mouvement(listebille4[colonnebille],False)
                    placementbille4[colonnebille]=False
                if placementbille3[colonnebille]==True:
                    initialise_mouvement(listebille3[colonnebille],False)
                    placementbille3[colonnebille]=False
                
                if placementbille2[colonnebille]==True:
                    initialise_mouvement(listebille2[colonnebille],False)
                    placementbille2[colonnebille]=False
                
                placementbille1[colonnebille]=False    
                initialise_mouvement(bille,False)
            else:
                initialise_mouvement(bille,True)
                placementbille1[colonnebille]=True
    if (numerobille=="2"):
            if (placementbille2[colonnebille]==True):
                if (placementbille4[colonnebille]==True):
                    initialise_mouvement(listebille4[colonnebille],False)
                    placementbille4[colonnebille]=False
                if placementbille3[colonnebille]==True:
                    initialise_mouvement(listebille3[colonnebille],False)
                    placementbille3[colonnebille]=False
                
                placementbille2[colonnebille]=False    
                initialise_mouvement(bille,False)


            else:
                if (placementbille1[colonnebille]==False):
                    initialise_mouvement(listebille1[colonnebille],True)
                    placementbille1[colonnebille]=True
                placementbille2[colonnebille]=True  
                initialise_mouvement(bille,True)
        
    if (numerobille=="3"):
            if (placementbille3[colonnebille]==True):
                if (placementbille4[colonnebille]==True):
                    initialise_mouvement(listebille4[colonnebille],False)
                    placementbille4[colonnebille]=False
                	
                placementbille3[colonnebille]=False    
                initialise_mouvement(bille,False)
            else:#On veut l'activer 
                if (placementbille1[colonnebille]==False):
                    initialise_mouvement(listebille1[colonnebille],True)
                    placementbille1[colonnebille]=True
                if (placementbille2[colonnebille]==False):
                    initialise_mouvement(listebille2[colonnebille],True)
                    placementbille2[colonnebille]=True
                placementbille3[colonnebille]=True  
                initialise_mouvement(bille,True)
                
    if (numerobille=="4"):
            if (placementbille4[colonnebille]==True):
                
                placementbille4[colonnebille]=False 
                initialise_mouvement(bille,False)
            else:
                if (placementbille1[colonnebille]==False):
                    initialise_mouvement(listebille1[colonnebille],True)
                    placementbille1[colonnebille]=True
                if (placementbille2[colonnebille]==False):
                    initialise_mouvement(listebille2[colonnebille],True)
                    placementbille2[colonnebille]=True
                if (placementbille3[colonnebille]==False):
                    initialise_mouvement(listebille3[colonnebille],True)
                    placementbille3[colonnebille]=True
                placementbille4[colonnebille]=True 
                initialise_mouvement(bille,True)
    affichage_chiffre(colonnebille)

def affichage_chiffre(colonnebille):
    global canvas
    global listechiffre
    """Donne la valeur des nombres sous chaque colonne"""

   
    chiffre=recup_chiffre(colonnebille)
    canvas.itemconfig(listechiffre[colonnebille], text=str(chiffre))
    
   
def recup_chiffre(colonnebille):
    
    chiffre=0

    if (placementbille5[colonnebille]==True):
        chiffre+=5
    if (placementbille1[colonnebille]==True):
        chiffre+=1

    if (placementbille2[colonnebille]==True):
        chiffre+=1

    if (placementbille3[colonnebille]==True):
        chiffre+=1

    if (placementbille4[colonnebille]==True):
        chiffre+=1
    return chiffre



def initialise_mouvement(bille,sens):
    """ Initialise les variables globales"""
    global canvas, racine
    canvas.itemconfig(bille, fill='white')
    global v
    for i in range(30):
        if sens==True :#on veut qu'elle monte
            canvas.move(bille,0,-1)
        if sens ==False:
            canvas.move(bille,0,+1)
        time.sleep(v)
        racine.update()
    
    canvas.itemconfig(bille, fill='red')


def augmente_vitesse():
    """Permet d'augmenter la vitesse d'une bille"""
    global v
    if v>0:
        v-=0.1

def baisse_vitesse():
    """Permet de diminuer la vitesse d'une bille"""
    global v
    v+=0.1



def choixcolonnes():
    n=len(listebille1)
    if n<14:
        creation_colonne(1000-70*n)



def creation_colonne(coordlignex0):
    """ Crée une colonne"""
    global listebille1,listebille2,listebille3,listebille4,listebille5
    global placementbille1, placementbille2,placementbille3,placementbille4,placementbille5
    global listechiffre
    global canvas
    chiffre="0"
    n=len(listebille1)
    

    
    canvas.create_line(coordlignex0,0,coordlignex0,250,fill="black", width=10)
    billequinaire=canvas.create_oval((coordlignex0-30),0,(coordlignex0+30),30, fill="red", tags=['5', str(n)])
    billeunaire1=canvas.create_oval((coordlignex0-30),(30*4),(coordlignex0+30),(30*5), fill="red", tags=['1', str(n)])
    billeunaire2=canvas.create_oval((coordlignex0-30),(30*5),(coordlignex0+30),(30*6), fill="red", tags=['2', str(n)])
    billeunaire3=canvas.create_oval((coordlignex0-30),(30*6),(coordlignex0+30),(30*7), fill="red", tags=['3', str(n)])
    billeunaire4=canvas.create_oval((coordlignex0-30),(30*7),(coordlignex0+30),(30*8), fill="red", tags=['4', str(n)])
    chiffresouscolonne=canvas.create_text(coordlignex0,30*9, text=chiffre,fill="black", font=40)
    



 

    listebille5.append(billequinaire)
    listebille1.append(billeunaire1)
    listebille2.append(billeunaire2)
    listebille3.append(billeunaire3)
    listebille4.append(billeunaire4)

    placementbille1.append(False)
    placementbille2.append(False)
    placementbille3.append(False)
    placementbille4.append(False)
    placementbille5.append(False)

    listechiffre.append(chiffresouscolonne)

def sauvegarde():
    fic = open("sauvegarde", "w")
    fic.write(str(recup_valeurboulier()))
    fic.close()
    

def recup_valeurboulier():
    """Permet de récuperer la valeur du boulier, on recpere la valeur de chaque colonne"""
    valeur_chiffre=0
    n=len(listebille1)
    for i in range(n):
        valeur_chiffre+=recup_chiffre(i)*(10**i)
    return valeur_chiffre

def position_bille(colonnebille,valeur):
    global listebille1,listebille2,listebille3,listebille4,listebille5
    global placementbille1, placementbille2,placementbille3,placementbille4,placementbille5

    if valeur>=5:
        if placementbille5[colonnebille]==False:
            deplacementdesbilles(colonnebille,"5",listebille5[colonnebille])
        valeur-=5
    else:
        if placementbille5[colonnebille]==True:
            deplacementdesbilles(colonnebille,"5",listebille5[colonnebille])



    if valeur==4:
        if placementbille4[colonnebille]==False:
            deplacementdesbilles(colonnebille,"4",listebille4[colonnebille])
        
    else:
        if placementbille4[colonnebille]==True:
            deplacementdesbilles(colonnebille,"4",listebille4[colonnebille])




    if valeur==3:
        if placementbille3[colonnebille]==False:
            deplacementdesbilles(colonnebille,"3",listebille3[colonnebille])
    elif valeur <3:
        if placementbille3[colonnebille]==True:
            deplacementdesbilles(colonnebille,"3",listebille3[colonnebille])



    if valeur==2:
        if placementbille2[colonnebille]==False:
            deplacementdesbilles(colonnebille,"2",listebille2[colonnebille])
    elif valeur <2:
        if placementbille2[colonnebille]==True:
            deplacementdesbilles(colonnebille,"2",listebille2[colonnebille])
    
    
    if valeur==1:
        if placementbille1[colonnebille]==False:
            deplacementdesbilles(colonnebille,"1",listebille1[colonnebille])
    elif valeur <1:
        if placementbille1[colonnebille]==True:
            deplacementdesbilles(colonnebille,"1",listebille1[colonnebille])


def load():
    """Charge la configuration sauvegardée et la retourne si
    elle a même valeur N que la config courante, sinon retourne config vide
    """
    fic = open("sauvegarde", "r")
    
    ligne = fic.readline()
    n=len(ligne)

    if n <= len(listebille1):
        for i in range(n):
            valeur=int(ligne[n-1-i])#de 0 à neuf 
            position_bille(i,valeur)


    



def reinitialisation_boulier():
    """Permet de reinitialiser le boulier"""
    global canvas

    

    n=len(listebille1)
    for colonnebille in range (n):
    
        if placementbille5[colonnebille]==True:
            deplacementdesbilles(colonnebille,"5",listebille5[colonnebille])
        
        if placementbille1[colonnebille]==True: 
            deplacementdesbilles(colonnebille,"1",listebille1[colonnebille])

##############################################################################################################################################
#OPERATIONS


def addition():
    """Permet d'aditionner les deux opérandes"""

    global racine
    global operande1, operande2
    valeur1=operande1.get()
    n=len(valeur1)

    if n <= len(listebille1):
        for i in range(n):
            valeurnum=int(valeur1[n-1-i])
            position_bille(i,valeurnum)
    valeur2=operande2.get()
    n2=len(valeur2)
    if n2 <= len(listebille1):
        for i in range(n2):
            valeurnum2=int(valeur2[i])
            if n2-i>n:
                position_bille(n2-i-1,valeurnum2)
            else:
                valeurnum1=int(valeur1[n-n2+i])
                if valeurnum1+valeurnum2 < 10:
                    position_bille(n2-i-1,valeurnum1+valeurnum2)
                else:
                    retenue=True
                    colonneretenue = n2-i
                    position_bille(n2-i-1,valeurnum1+valeurnum2-10)
                    while retenue:
                        valeur0 = recup_chiffre(colonneretenue)
                        if valeur0 < 9:
                            position_bille(colonneretenue,valeur0+1)
                            retenue=False
                        else:
                            position_bille(colonneretenue,0)
                            colonneretenue = colonneretenue + 1

def soustraction():
    """Permet de soustraire les deux opérandes"""

    global racine
    global operande1, operande2
    valeur1=operande1.get()
    n=len(valeur1)

    if n <= len(listebille1):
        for i in range(n):
            valeurnum=int(valeur1[n-1-i])
            position_bille(i,valeurnum)
    valeur2=operande2.get()
    n2=len(valeur2)
    if n2 <= len(listebille1):
        for i in range(n2):
            valeurnum2=int(valeur2[i])
            if n2-i>n:
                position_bille(n2-i-1,valeurnum2)
            else:
                valeurnum1=int(valeur1[n-n2+i])
                if valeurnum1+valeurnum2 < 10:
                    position_bille(n2-i-1,valeurnum1-valeurnum2)
                else:
                    retenue=True
                    colonneretenue = n2-i
                    position_bille(n2-i-1,valeurnum1-valeurnum2-10)
                    while retenue:
                        valeur0 = recup_chiffre(colonneretenue)
                        if valeur0 < 9:
                            position_bille(colonneretenue,valeur0+1)
                            retenue=False
                        else:
                            position_bille(colonneretenue,0)
                            colonneretenue = colonneretenue + 1
      







 

#######################
# programme principal

racine=tk.Tk()
racine.title("Soroban")
canvas=tk.Canvas(racine,width=1050,height=300,  bg="white")
ligne2=canvas.create_line(0,75,1050,75, fill="black", width=30)
bouton1 = tk.Button(text="Augmente Vitesse", command=augmente_vitesse)
bouton2 = tk.Button(text="Baisse Vitesse", command=baisse_vitesse)
bouton3 = tk.Button(text="Nombre de colonnes", command=choixcolonnes)
bouton4 = tk.Button(text="Reinitialiser", command=reinitialisation_boulier)
bouton5 = tk.Button(text="Enregistrer", command=sauvegarde)
bouton6 = tk.Button(text="Charger", command=load)
bouton7 = tk.Button(text="Additionner", command=addition)
bouton8 = tk.Button(text="Soustraire", command=soustraction)
operande1=tk.Entry(racine)
operande2=tk.Entry(racine)





######################
#Appel de fonctions

creation_colonne(1000)


######################
#Placement des widget
canvas.grid()
bouton1.place(x = 20,y = 305) 
bouton2.place(x = 20,y = 330) 
bouton3.place(x = 200,y = 330)
bouton4.place(x = 940,y = 330) 
bouton5.place(x = 940,y = 305) 
bouton6.place(x = 800,y = 330) 
bouton7.place(x = 650,y = 305)
bouton8.place(x = 650,y = 330)
operande1.grid()
operande2.grid()

######################
#Gestion des evenements
racine.bind("<Button-1>",clic)

#######################
#Lancement de la boucle principale'
racine.mainloop()