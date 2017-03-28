#Modules

from tkinter import * # On importe les modules Tkinter pour l'interface graphique , random pour le choix de nombres aléatoires et tkinter.messagebox pour l'apparition d'alertes

import random

from tkinter.messagebox import *

#Définition des fonctions

t=0                     # On initialise t à t=0. La variable t est 
def com0 () :
    global x,t          # On met les variables x et t en global
    x=0                 # On met x à la valeur du bouton que l'on veut
    t=t*10+x            # On multiplie t par 10 pour passer des unités ,aux centaines aux milliers ...
    var.set(str(t))     # On assigne à la variable var (qui correspond à la la variable ligne_result ,qui ajoute t à l'Entry

def com1() :
    global x,t          # De même ...
    x=1
    t=t*10+x
    var.set(str(t))

def com2 () :
    global x,t,var
    x=2
    t=t*10+x
    var.set(str(t))

def com3 () :
    global x,t
    x=3
    t=t*10+x
    var.set(str(t))

def com4 () :
    global x,t
    x=4
    t=t*10+x
    var.set(str(t))

def com5 () :
    global x,t
    x=5
    t=t*10+x
    var.set(str(t))

def com6 () :
    global x,t
    x=6
    t=t*10+x
    var.set(str(t))

def com7 () :
    global x,t
    x=7
    t=t*10+x
    var.set(str(t))

def com8 () :
    global x,t
    x=8
    t=t*10+x
    var.set(str(t))

def com9 () :
    global x,t
    x=9
    t=t*10+x
    var.set(str(t))

def eff():
    global x,t
    t=0
    var.set(str(t))
    


def exe():                                      # Fonction bouton Exe qui permet de valider un résultat
    global b,selection,addition,soustraction,multiplication,score,niveau

    reponse=int(ligne_result.get())        #Dans la variable reponse ,on met ce qui a été saisi par l'utilisateur dans ligne_result
    
    if selection==0:               #La variable selection permet de savoir s'il faut vérifier une somme , une différence ou un produit. Si elle vaut 0 ,aucune opération n'a été choisie 
        showinfo("Alerte","Choisissez d'abord une opération ! :)")           # Dans ce cas ,une alerte apparaît
    elif selection==1:              
        
        if reponse==addition:        # On vérifie si le résultat est juste
            score=score+1       # On rajoute 1 au score
            niveauplus()      # La fonction niveauplus vérifie si le score est égal à 5
            addi()            # La prochaine addition s'affiche
            eff()             # La dernière réponse de l'utilisateur s'efface
            VraiFaux=Label(fenetre,bg="dark grey",text="VRAI",fg="green",font=font,width=5).grid(row=2,column=2)   # On affiche VRAI

        else:
            score=score-1                      # On enlève 1 au score
            niveauplus()                        # De même ...
            addi()
            eff()
            VraiFaux=Label(fenetre,bg="dark grey",text="FAUX",fg="red",font=font,width=5).grid(row=2,column=2)    # On affiche FAUX  
            result_affichage=Label(fenetre,bg="dark grey",text=resultaddi()).grid(row=3,column=2)

    elif selection==2:

        if reponse==soustraction:
            score=score+1                       
            niveauplus()
            sous()
            eff()
            VraiFaux=Label(fenetre,bg="dark grey",text="VRAI",fg="green",font=font,width=5).grid(row=2,column=2)
            

        else:
            score=score-1                       
            niveauplus()
            sous()
            eff()
            VraiFaux=Label(fenetre,bg="dark grey",text="FAUX",fg="red",font=font,width=5).grid(row=2,column=2)

    elif selection==3:

        if reponse==multiplication:       
            score=score+1                      
            niveauplus()
            multi()
            eff()
            VraiFaux=Label(fenetre,bg="dark grey",text="VRAI",fg="green",font=font,width=5).grid(row=2,column=2)

        else:
            score=score-1                       
            niveauplus()
            multi()
            eff()
            VraiFaux=Label(fenetre,bg="dark grey",text="FAUX",fg="red",font=font,width=5).grid(row=2,column=2)

    score_affichage=Label(fenetre,bg="orange",text=str(score)).grid(row=2,column=4)
      

def niveauplus():                      # La fonction vérifie si le score vaut 5 et s'il faut monter de niveau
    global score,niveau
    if score==5:                        # Si le score est égal à 5 ...
        niveau=niveau+1                 # On passe au niveau suivant
        score=0                         # Le score est réinitialisé à 0
        niveau_affichage=Label(fenetre,bg="orange",text=str(niveau)).grid(row=2,column=5)   # On affiche le niveau
        
        
def addi():
    global score,niveau,selection,addition
    selection=1             # On affecte à selection la valeur 1 qui signifie "c'est une addition"
    if niveau==1:          # Le programme vérifie à quel niveau est l'utilisateur

        premiernombreaddi=random.randint(0,10)    # Le premier nombre est choisi aléatoirement
        derniernombreaddi=random.randint(0,10)    # Le second nombre est choisi aléatoirement  
        addition=premiernombreaddi+derniernombreaddi         # La variable addition est la somme des deux nombres et permettra de vérifier la réponse de l'utilisateur
        addition_str=str(premiernombreaddi),'+' ,str(derniernombreaddi) ,'='    # On transforme en chaîne de caractère
        ligne_calcul=Label(fenetre,text=addition_str,width=40,font=font2).grid(row=1,column=3)  # On l'affiche pour l'utilisateur
        
        
    elif niveau==2:

        premiernombreaddi=random.randint(10,100) 
        derniernombreaddi=random.randint(0,10) 
        addition=premiernombreaddi+derniernombreaddi
        addition_str=str(premiernombreaddi),"+" ,str(derniernombreaddi) ,"=" 
        ligne_calcul=Label(fenetre,text=addition_str,width=40,font=font2).grid(row=1,column=3)  # On l'affiche pour l'utilisateur

    
    elif niveau==3:

        premiernombreaddi=random.randint(10,100) 
        derniernombreaddi=random.randint(10,100) 
        addition=premiernombreaddi+derniernombreaddi
        addition_str=str(premiernombreaddi),"+" ,str(derniernombreaddi) ,"=" 
        ligne_calcul=Label(fenetre,text=addition_str,width=40,font=font2).grid(row=1,column=3)  # On l'affiche pour l'utilisateur

    
    elif niveau==4:

        premiernombreaddi=random.randint(100,1000) 
        derniernombreaddi=random.randint(10,100) 
        addition=premiernombreaddi+derniernombreaddi
        addition_str=str(premiernombreaddi),"+" ,str(derniernombreaddi) ,"=" 
        ligne_calcul=Label(fenetre,text=addition_str,width=40,font=font2).grid(row=1,column=3)  # On l'affiche pour l'utilisateur
 

    
    elif niveau==5:

        premiernombreaddi=random.randint(100,1000) 
        derniernombreaddi=random.randint(100,1000) 
        addition=premiernombreaddi+derniernombreaddi
        addition_str=str(premiernombreaddi),"+" ,str(derniernombreaddi) ,"=" 
        ligne_calcul=Label(fenetre,text=addition_str,width=40,font=font2).grid(row=1,column=3)  # On l'affiche pour l'utilisateur

    
    
def sous():
    global score,niveau,selection,soustraction                 #Même chose pour la soustraction
    selection=2     # On affecte à selection la valeur 1 qui signifie "c'est une soustraction"
    if niveau==1:

        premiernombresous=random.randint(0,10) 
        derniernombresous=random.randint(0,premiernombresous)
        soustraction=premiernombresous-derniernombresous
        soustraction_str=str(premiernombresous),"-" ,str(derniernombresous) ,"=" 
        ligne_calcul=Label(fenetre,text=soustraction_str,width=40,font=font2).grid(row=1,column=3)  # On l'affiche pour l'utilisateur



    
    elif niveau==2:

        premiernombresous=random.randint(10,100) 
        derniernombresous=random.randint(10,premiernombresous) 
        soustraction=premiernombresous-derniernombresous
        soustraction_str=str(premiernombresous),"-" ,str(derniernombresous) ,"=" 
        ligne_calcul=Label(fenetre,text=soustraction_str,width=40,font=font2).grid(row=1,column=3)  # On l'affiche pour l'utilisateur

    
    elif niveau==3:

        premiernombresous=random.randint(10,200) 
        derniernombresous=random.randint(10,premiernombresous) 
        soustraction=premiernombresous-derniernombresous
        soustraction_str=str(premiernombresous),"-" ,str(derniernombresous) ,"=" 
        ligne_calcul=Label(fenetre,text=soustraction_str,width=40,font=font2).grid(row=1,column=3)  # On l'affiche pour l'utilisateur


    
    elif niveau==4:

        premiernombresous=random.randint(50,500) 
        derniernombresous=random.randint(50,premiernombresous) 
        soustraction=premiernombresous-derniernombresous
        soustraction_str=str(premiernombresous),"-" ,str(derniernombresous) ,"=" 
        ligne_calcul=Label(fenetre,text=soustraction_str,width=40,font=font2).grid(row=1,column=3)  # On l'affiche pour l'utilisateur


    
    elif niveau==5:

        premiernombresous=random.randint(100,1000) 
        derniernombresous=random.randint(100,premiernombresous) 
        soustraction=premiernombresous-derniernombresous
        soustraction_str=str(premiernombresous),"-" ,str(derniernombresous) ,"=" 
        ligne_calcul=Label(fenetre,text=soustraction_str,width=40,font=font2).grid(row=1,column=3)  # On l'affiche pour l'utilisateur

    
def multi():
    global score,niveau,selection,multiplication
    selection=3         # On affecte à selection la valeur 1 qui signifie "c'est une multiplication"
    if niveau==1:

        premiernombremulti=random.randint(0,10) 
        derniernombremulti=random.randint(0,10) 
        multiplication=premiernombremulti*derniernombremulti                              #Mêmes instructions pour la multiplication
        multiplication_str=str(premiernombremulti),"x" ,str(derniernombremulti) ,"=" 
        ligne_calcul=Label(fenetre,text=multiplication_str,width=40,font=font2).grid(row=1,column=3)  # On l'affiche pour l'utilisateur



    
    elif niveau==2:

        premiernombremulti=random.randint(1,21) 
        derniernombremulti=random.randint(1,21) 
        multiplication=premiernombremulti*derniernombremulti
        multiplication_str=str(premiernombremulti),"x" ,str(derniernombremulti) ,"="
        ligne_calcul=Label(fenetre,text=multiplication_str,width=40,font=font2).grid(row=1,column=3)  # On l'affiche pour l'utilisateur

    
    elif niveau==3:

        premiernombremulti=random.randint(1,10) 
        derniernombremulti=random.randint(1,51) 
        multiplication=premiernombremulti*derniernombremulti
        multiplication_str=str(premiernombremulti),"x" ,str(derniernombremulti) ,"="
        ligne_calcul=Label(fenetre,text=multiplication_str,width=40,font=font2).grid(row=1,column=3)  # On l'affiche pour l'utilisateur

    
    elif niveau==4:

        premiernombremulti=random.randint(10,51) 
        derniernombremulti=random.randint(10,51) 
        multiplication=premiernombremulti*derniernombremulti
        multiplication_str=str(premiernombremulti),"x" ,str(derniernombremulti) ,"="
        ligne_calcul=Label(fenetre,text=multiplication_str,width=40,font=font2).grid(row=1,column=3)  # On l'affiche pour l'utilisateur
    

    

    elif niveau==5:

        premiernombremulti=random.randint(10,100) 
        derniernombremulti=random.randint(10,100) 
        multiplication=premiernombremulti*derniernombremulti
        multiplication_str=str(premiernombremulti),"x" ,str(derniernombremulti) ,"="
        ligne_calcul=Label(fenetre,text=multiplication_str,width=40,font=font2).grid(row=1,column=3)  # On l'affiche pour l'utilisateur

def niv1():
    global niveau,score,selection
    niveau=1
    score=0
    if selection == 0:
        showinfo("Alerte","Choisissez d'abord une opération ! :)")
        niveau=1
    elif selection == 1:
        addi()
    elif selection == 2:
        sous()
    elif selection == 3:
        multi()
    niveau_affichage=Label(fenetre,bg="orange",text=str(niveau)).grid(row=2,column=5)
    score_affichage=Label(fenetre,bg="orange",text=str(score)).grid(row=2,column=4)

def niv2():
    global niveau,score,selection
    niveau=2
    score=0
    if selection == 0:
        showinfo("Alerte","Choisissez d'abord une opération ! :)")
        niveau=1
    elif selection == 1:
        addi()
    elif selection == 2:
        sous()
    elif selection == 3:
        multi()
    niveau_affichage=Label(fenetre,bg="orange",text=str(niveau)).grid(row=2,column=5)
    score_affichage=Label(fenetre,bg="orange",text=str(score)).grid(row=2,column=4)

def niv3():
    global niveau,score,selection
    niveau=3
    score=0
    if selection == 0:
        showinfo("Alerte","Choisissez d'abord une opération! :)")
        niveau=1
    elif selection == 1:
        addi()
    elif selection == 2:
        sous()
    elif selection == 3:
        multi()
    niveau_affichage=Label(fenetre,bg="orange",text=str(niveau)).grid(row=2,column=5)
    score_affichage=Label(fenetre,bg="orange",text=str(score)).grid(row=2,column=4)

def niv4():
    global niveau,score,selection
    niveau=4
    score=0
    if selection == 0:
        showinfo("Alerte","Choisissez d'abord une opération ! :)")
        niveau=1
    elif selection == 1:
        addi()
    elif selection == 2:
        sous()
    elif selection == 3:
        multi()
    niveau_affichage=Label(fenetre,bg="orange",text=str(niveau)).grid(row=2,column=5)
    score_affichage=Label(fenetre,bg="orange",text=str(score)).grid(row=2,column=4)


def niv5():
    global niveau,score,selection
    niveau=5
    score=0
    if selection == 0:
        showinfo("Alerte","Choisissez d'abord une opération ! :)")
        niveau=1
    elif selection == 1:
        addi()
    elif selection == 2:
        sous()
    elif selection == 3:
        multi()
    niveau_affichage=Label(fenetre,bg="orange",text=str(niveau)).grid(row=2,column=5)
    score_affichage=Label(fenetre,bg="orange",text=str(score)).grid(row=2,column=4)







def initialisation():          #Commande pour recommencer
    global niveau,score,selection
    niveau=1
    score=0
    if selection == 0:
        showinfo("Alerte","Choisissez d'abord une opération ! :)")
    elif selection == 1:
        addi()
    elif selection == 2:
        sous()
    elif selection == 3:
        multi()
    niveau_affichage=Label(fenetre,bg="orange",text=str(niveau)).grid(row=2,column=5)
    score_affichage=Label(fenetre,bg="orange",text=str(score)).grid(row=2,column=4)

    
#Programme

    #Initialisation du niveau et du score

niveau=1 # Le niveau est initialisé à 1
score=0        # Le score est initialisé à 0
selection=0 #Lorsque selection vaut 0 , l'utilisateur recevra un message comme quoi il doit choisir une opération

    # Interface Tkinter

font= ("Jokerman",20)
font2= ("Corbel",10)
font3=("Corbel",12)
fenetre=Tk()
fenetre.title("Little Professor")
fond = Canvas(fenetre,height=586,width=586,bg="dark grey").grid(row=0,column=0,rowspan=12,columnspan=10)      
texte= Label(fenetre ,text="LITTLE PROFESSOR !", font=font ,fg="blue",bg="dark grey").grid(row=0,column=3)

ligne_calcul = Label(fenetre,text="Bonjour. Choisissez l'opération puis le niveau" ,bg="orange",width=40,font=font2).grid(row=1,column=3)
score_label=Label(fenetre,text="Score",bg="bisque",font=font3).grid(row=1,column=4)
niveau_label=Label(fenetre,text="Niveau",bg="bisque",font=font3).grid(row=1,column=5)

var = StringVar()
ligne_result = Entry(fenetre,bg="orange", textvariable=var)
ligne_result.grid(row=2,column=3)
niveau_affichage=Label(fenetre,bg="orange",text="1").grid(row=2,column=5)
score_affichage=Label(fenetre,bg="orange",text="0").grid(row=2,column=4)
VraiFaux=Label(fenetre,bg="dark grey",text="",font=font).grid(row=2,column=2)
var.set("Bienvenue sur LP")


fra1 = Frame(bg="dark grey")
fra1.grid(row=3,column=3)
Button(fra1, text = '1', command= com1).grid(row=2, column = 0, padx = 3, pady = 3)
Button(fra1, text = '2', command= com2).grid(row=2, column = 1, padx = 3, pady = 3)
Button(fra1, text = '3', command= com3).grid(row=2, column = 2, padx = 3, pady = 3)
Button(fra1, text = '4', command= com4).grid(row=3, column = 0, padx = 3, pady = 3)
Button(fra1, text = '5', command= com5).grid(row=3, column = 1, padx = 3, pady = 3)
Button(fra1, text = '6', command= com6).grid(row=3, column = 2, padx = 3, pady = 3)
Button(fra1, text = '7', command= com7).grid(row=4, column = 0, padx = 3, pady = 3)
Button(fra1, text = '8', command= com8).grid(row=4, column = 1, padx = 3, pady = 3)
Button(fra1, text = '9', command= com9).grid(row=4, column = 2, padx = 3, pady = 3)
Button(fra1, text = '0', command= com0).grid(row=5, column = 1, padx = 3, pady = 3)
Button(fra1, text = 'Eff', command= eff ).grid(row=5, column = 2, padx = 3, pady = 3)
Button(fra1, text = 'Exe', command= exe).grid(row=5, column = 0, padx = 3, pady = 3)

operation_choix= Label(fenetre,text="Choix de l'operation",bg="orange",font=font3).grid(row=7,column=3)
bouton_addi = Button(ligne_calcul, text="Addition",command=addi).grid(row=8,column=2) 
bouton_sous = Button(fenetre, text="Soustraction",command=sous).grid(row=8,column=3)
bouton_multi = Button(fenetre, text="Multiplication",command=multi).grid(row=8,column=4)


fra2 = Frame(bg="dark grey")
fra2.grid(row=10,column=3)

niveau_choix= Label(fenetre,text="Choix du niveau",bg="orange",font=font3).grid(row=9,column=3)
Niveau_1 = Button(fra2,text="1",command=niv1).grid(row=1,column=1, padx = 3)
Niveau_2 = Button(fra2,text="2",command=niv2).grid(row=1,column=2, padx = 3)
Niveau_3 = Button(fra2,text="3",command=niv3).grid(row=1,column=3, padx = 3)
Niveau_4 = Button(fra2,text="4",command=niv4).grid(row=1,column=4, padx = 3)
Niveau_5 = Button(fra2,text="5",command=niv5).grid(row=1,column=5, padx = 3)

reset = Button(fenetre,text="Reset",command=initialisation).grid(row=11,column=2)
quitter = Button(fenetre, text="Quitter", command=fenetre.destroy,).grid(row=11,column=4)

fenetre.mainloop()






