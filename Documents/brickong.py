#!/usr/bin/env python3

from tkinter import * #On importe le module graphique Tkinter

def Casse_brique(): #Fonction Casse-Brique
    global coords, x, y, delta_x, delta_y, nb_brique, test_brique0, test_brique1, test_brique2, test_brique3, test_brique4, test_brique5, test_brique6, test_brique7, test_brique8, test_brique9

    delta_x = 1                 #variable de la balle en abscisse
    delta_y = -1                #variable de la balle en ordonnée
    x = 300                     #postion en abscisse
    y = 560                     #postion en ordonnée
    coords = (250, 570)         #position initiale de la raquette en (x , y)
    test_brique0 = 1            #booléen qui vérifie si la brique est présente dans l'écran ou non
    test_brique1 = 1            #10 test_brique car 10 briques
    test_brique2 = 1
    test_brique3 = 1
    test_brique4 = 1
    test_brique5 = 1
    test_brique6 = 1
    test_brique7 = 1
    test_brique8 = 1
    test_brique9 = 1
    nb_brique = 10              #variable comptant le nombre de brique restante à l'écran

                                #Balle

    def deplacement():          #Fonction déplaçant la balle et réalisant les tests de collision de brique

        global x, y, delta_x, delta_y, nb_brique, test_brique0, test_brique1, test_brique2, test_brique3, test_brique4, test_brique5, test_brique6, test_brique7, test_brique8, test_brique9

        if x == 0:              #Rebond de la balle coté gauche
            delta_x = 1

        if x + 10 == 600:       #Rebond de la balle coté droit
            delta_x = -1

        if y + 10 == 570 and x >= coords[0] and x <= coords[0]+25:  #Rebond de la balle coté gauche de la raquette
            delta_y = -1
            delta_x = -1

        if y + 10 == 570 and x >= coords[0]+25 and x <= coords[0]+75: #Rebond de la balle au milieu de la raquette
            delta_y = -1

        if y + 10 == 570 and x >= coords[0]+75 and x <= coords[0]+100: #Rebond de la balle coté droit de la raquette
            delta_y = -1
            delta_x = 1

        if y == 0:              #Rebond de la balle en haut
            delta_y = 1

        if y + 10 > 570:        #Sortie de l'écran -> fin de la partie
             canvas.coords(gameover, 300, 150)
             canvas.coords(restart, 300,250)

                                #Brique 0

        if y == 125 and x >= 40 and x <= 140 and test_brique0 == 1:         #Si la balle rebondit sur le bas de la brique
            delta_y = 1                                                     #Elle rebondit, donc se déplace vers le bas
            canvas.coords(brique0,1000,1000,1000,1000)                      #La brique est déplacée en dehors de l'écran
            test_brique0 = 0                                                #Elle n'est plus présente à l'écran
            nb_brique -= 1                                                  #Il y a une brique en moins à l'écran

        if y + 10 == 100 and x >= 40 and x <= 140 and test_brique0 == 1:    #Si la balle rebondit sur le haut de la brique
            delta_y = -1
            canvas.coords(brique0,1000,1000,1000,1000)
            test_brique0 = 0
            nb_brique -= 1

        if x == 140 and y >= 100 and y <= 125 and test_brique0 == 1:        #Si la balle rebondit sur la droite de la brique
            delta_x = 1
            canvas.coords(brique0,1000,1000,1000,1000)
            test_brique0 = 0
            nb_brique -= 1

        if x + 10 == 40 and y >= 100 and y <= 125 and test_brique0 == 1:    #Si la balle rebondit sur la gauche de la brique
            delta_x = -1
            canvas.coords(brique0,1000,1000,1000,1000)
            test_brique0 = 0
            nb_brique -= 1

                                #Brique 1

        if y == 125 and x >= 180 and x <= 280 and test_brique1 == 1:        #Ces boucles fonctionnent de la même manière
            delta_y = 1
            canvas.coords(brique1,1000,1000,1000,1000)
            test_brique1 = 0
            nb_brique -= 1

        if y + 10 == 100 and x >= 180 and x <= 280 and test_brique1 == 1:
            delta_y = -1
            canvas.coords(brique1,1000,1000,1000,1000)
            test_brique1 = 0
            nb_brique -= 1

        if x == 280 and y >= 100 and y <= 125 and test_brique1 == 1:
            delta_x = 1
            canvas.coords(brique1,1000,1000,1000,1000)
            test_brique1 = 0
            nb_brique -= 1

        if x + 10 == 180 and y >= 100 and y <= 125 and test_brique1 == 1:
            delta_x = -1
            canvas.coords(brique1,1000,1000,1000,1000)
            test_brique1 = 0
            nb_brique -= 1

                                #Brique 2

        if y == 125 and x >= 320 and x <= 420 and test_brique2 == 1:
            delta_y = 1
            canvas.coords(brique2,1000,1000,1000,1000)
            test_brique2 = 0
            nb_brique -= 1

        if y + 10 == 100 and x >= 320 and x <= 420 and test_brique2 == 1:
            delta_y = -1

            canvas.coords(brique2,1000,1000,1000,1000)

            test_brique2 = 0

            nb_brique -= 1

        if x == 420 and y >= 100 and y <= 125 and test_brique2 == 1:

            delta_x = 1

            canvas.coords(brique2,1000,1000,1000,1000)

            test_brique2 = 0

            nb_brique -= 1


        if x + 10 == 320 and y >= 100 and y <= 125 and test_brique2 == 1:
            delta_x = -1
            canvas.coords(brique2,1000,1000,1000,1000)
            test_brique2 = 0
            nb_brique -= 1

                                #Brique 3

        if y == 125 and x >= 460 and x <= 560 and test_brique3 == 1:
            delta_y = 1
            canvas.coords(brique3,1000,1000,1000,1000)
            test_brique3 = 0
            nb_brique -= 1

        if y + 10 == 100 and x >= 460 and x <= 560 and test_brique3 == 1:
            delta_y = -1
            canvas.coords(brique3,1000,1000,1000,1000)
            test_brique3 = 0
            nb_brique -= 1

        if x == 560 and y >= 100 and y <= 125 and test_brique3 == 1:
            delta_x = 1
            canvas.coords(brique3,1000,1000,1000,1000)
            test_brique3 = 0
            nb_brique -= 1

        if x + 10 == 460 and y >= 100 and y <= 125 and test_brique3 == 1:
            delta_x = -1
            canvas.coords(brique3,1000,1000,1000,1000)
            test_brique3 = 0
            nb_brique -= 1

                                #Brique 4

        if y == 225 and x >= 40 and x <= 140 and test_brique4 == 1:
            delta_y = 1
            canvas.coords(brique4,1000,1000,1000,1000)
            test_brique4 = 0
            nb_brique -= 1

        if y + 10 == 200 and x >= 40 and x <= 140 and test_brique4 == 1:
            delta_y = -1
            canvas.coords(brique4,1000,1000,1000,1000)
            test_brique4 = 0
            nb_brique -= 1

        if x == 140 and y >= 200 and y <= 225 and test_brique4 == 1:
            delta_x = 1
            canvas.coords(brique4,1000,1000,1000,1000)
            test_brique4 = 0
            nb_brique -= 1

        if x + 10 == 40 and y >= 200 and y <= 225 and test_brique4 == 1:
            delta_x = -1
            canvas.coords(brique4,1000,1000,1000,1000)
            test_brique4 = 0
            nb_brique -= 1

                                #Brique 5

        if y == 225 and x >= 180 and x <= 280 and test_brique5 == 1:
            delta_y = 1
            canvas.coords(brique5,1000,1000,1000,1000)
            test_brique5 = 0
            nb_brique -= 1

        if y + 10 == 200 and x >= 180 and x <= 280 and test_brique5 == 1:
            delta_y = -1
            canvas.coords(brique5,1000,1000,1000,1000)
            test_brique5 = 0
            nb_brique -= 1

        if x == 280 and y >= 200 and y <= 225 and test_brique5 == 1:
            delta_x = 1
            canvas.coords(brique5,1000,1000,1000,1000)
            test_brique5 = 0
            nb_brique -= 1

        if x + 10 == 180 and y >= 200 and y <= 225 and test_brique5 == 1:
            delta_x = -1
            canvas.coords(brique5,1000,1000,1000,1000)
            test_brique5 = 0
            nb_brique -= 1

                                #Brique 6

        if y == 225 and x >= 320 and x <= 420 and test_brique6 == 1:
            delta_y = 1
            canvas.coords(brique6,1000,1000,1000,1000)
            test_brique6 = 0
            nb_brique -= 1

        if y + 10 == 200 and x >= 320 and x <= 420 and test_brique6 == 1:
            delta_y = -1
            canvas.coords(brique6,1000,1000,1000,1000)
            test_brique6 = 0
            nb_brique -= 1

        if x == 420 and y >= 200 and y <= 225 and test_brique6 == 1:
            delta_x = 1
            canvas.coords(brique6,1000,1000,1000,1000)
            test_brique6 = 0
            nb_brique -= 1

        if x + 10 == 320 and y >= 200 and y <= 225 and test_brique6 == 1:
            delta_x = -1
            canvas.coords(brique6,1000,1000,1000,1000)
            test_brique6 = 0
            nb_brique -= 1

                                #Brique 7

        if y == 225 and x >= 460 and x <= 560 and test_brique7 == 1:
            delta_y = 1
            canvas.coords(brique7,1000,1000,1000,1000)
            test_brique7 = 0
            nb_brique -= 1

        if y + 10 == 200 and x >= 460 and x <= 560 and test_brique7 == 1:
            delta_y = -1
            canvas.coords(brique7,1000,1000,1000,1000)
            test_brique7 = 0
            nb_brique -= 1

        if x == 560 and y >= 200 and y <= 225 and test_brique7 == 1:
            delta_x = 1
            canvas.coords(brique7,1000,1000,1000,1000)
            test_brique7 = 0
            nb_brique -= 1

        if x + 10 == 460 and y >= 200 and y <= 225 and test_brique7 == 1:
            delta_x = -1
            canvas.coords(brique7,1000,1000,1000,1000)
            test_brique7 = 0
            nb_brique -= 1

                                #Brique 8

        if y == 325 and x >= 180 and x <= 280 and test_brique8 == 1:
            delta_y = 1
            canvas.coords(brique8,1000,1000,1000,1000)
            test_brique8 = 0
            nb_brique -= 1

        if y + 10 == 300 and x >= 180 and x <= 280 and test_brique8 == 1:
            delta_y = -1
            canvas.coords(brique8,1000,1000,1000,1000)
            test_brique8 = 0
            nb_brique -= 1

        if x == 280 and y >= 300 and y <= 325 and test_brique8 == 1:
            delta_x = 1
            canvas.coords(brique8,1000,1000,1000,1000)
            test_brique8 = 0
            nb_brique -= 1

        if x + 10 == 180 and y >= 300 and y <= 325 and test_brique8 == 1:
            delta_x = -1
            canvas.coords(brique8,1000,1000,1000,1000)
            test_brique8 = 0
            nb_brique -= 1

                                #Brique 9

        if y == 325 and x >= 320 and x <= 420 and test_brique9 == 1:
            delta_y = 1
            canvas.coords(brique9,1000,1000,1000,1000)
            test_brique9 = 0
            nb_brique -= 1

        if y + 10 == 300 and x >= 320 and x <= 420 and test_brique9 == 1:
            delta_y = -1
            canvas.coords(brique9,1000,1000,1000,1000)
            test_brique9 = 0
            nb_brique -= 1

        if x == 420 and y >= 300 and y <= 325 and test_brique9 == 1:
            delta_x = 1
            canvas.coords(brique9,1000,1000,1000,1000)
            test_brique9 = 0
            nb_brique -= 1

        if x + 10 == 320 and y >= 300 and y <= 325 and test_brique9 == 1:
            delta_x = -1
            canvas.coords(win,300, 300)
            test_brique9 = 0
            nb_brique -= 1

                                #Fin du jeu

        if nb_brique == 0 :                     #si il n'y a plus de brique à l'écran
            canvas.coords(win, 300,150)         #on affiche "You win"
            canvas.coords(restart, 300,250)     #on affiche "Appuyez sur R pour recommencer"
            delta_x = 0                         #On stoppe la balle
            delta_y = 0

        x = x + delta_x                             #On ajoute à la coordonnée en abscisse la variation en abscisse (-1 ou 1)
        y = y + delta_y                             #On ajoute à la coordonnée en ordonnée la variation en ordonnée (-1 ou 1)
        casse_brique.after(5,deplacement)           #La fonction after execute toutes les x millisecondes la fonction déplacement
        canvas.coords(balle, x, y, x + 10, y + 10)  #On affiche la balle à ses nouvelles coordonnées

                                #Mouvements de la raquette

    def clavier(event):     #Fonction gérant le déplacement de la raquette avec les flèches, et la touche pour recommencer

        global coords, x, y, delta_x, delta_y, nb_brique, test_brique0, test_brique1, test_brique2, test_brique3, test_brique4, test_brique5, test_brique6, test_brique7, test_brique8, test_brique9

        touche = event.keysym   #variable récuperant l'état d'une touche

        if touche == "Right" and coords[0] != 500:  #Si on presse la flèche droite et que la raquette n'est pas à droite de l'écran
            coords = (coords[0] + 10, 570)          #La raquette se déplace de +10 pixels en abscisse

        if touche == "Left" and coords[0] != 0:     #Si on presse la flèche gauche et que la raquette n'est pas à gauche de l'écran
            coords = (coords[0] - 10, 570)          #La raquette se déplace de -10 pixels en abscisse

        canvas.coords(raquette, coords[0], 570, coords[0] + 100, 580)   #On affiche la raquette à ses nouvelles coordonnées

        if touche == "Escape" :                     #Si on appuie sur échap, la fenêtre se ferme, on revient au menu
            casse_brique.destroy()                  #La fenêtre se ferme, on revient au menu

        if (touche == 'r' and y + 10 >= 590) or (touche == 'r' and nb_brique == 0) :    #si on appuie sur R et que la balle est sortie de l'écran, ou si on appuie sur R et qu'il n'y a plus de brique à l'écran

           delta_x = 1      #On réinitialise les différents coordonnées
           delta_y = -1
           x = 300
           y = 560
           test_brique0 = 1
           test_brique1 = 1
           test_brique2 = 1
           test_brique3 = 1
           test_brique4 = 1
           test_brique5 = 1
           test_brique6 = 1
           test_brique7 = 1
           test_brique8 = 1
           test_brique9 = 1
           nb_brique = 10

           canvas.coords(win, 1000,1000)
           canvas.coords(gameover, 1000,1000)
           canvas.coords(restart, 1000,1000)

           canvas.coords(brique0, 40, 100, 140, 125)
           canvas.coords(brique1, 180, 100, 280, 125)
           canvas.coords(brique2, 320, 100, 420, 125)
           canvas.coords(brique3, 460, 100, 560, 125)

           canvas.coords(brique4, 40, 200, 140, 225)
           canvas.coords(brique5, 180, 200, 280, 225)
           canvas.coords(brique6, 320, 200, 420, 225)
           canvas.coords(brique7, 460, 200, 560, 225)

           canvas.coords(brique8, 180, 300, 280, 325)
           canvas.coords(brique9, 320, 300, 420, 325)

                                #Création de la fenêtre

    casse_brique = Tk()     #On ouvre une fenêtre Tkinter
    casse_brique.title("Casse Brique")
    casse_brique.geometry("600x600")

    canvas = Canvas(casse_brique, width=600, height=600, bg = "burlywood4")     #On crée un canvas de la même taille qyue la fenêtre
    canvas.pack()

    raquette = canvas.create_rectangle(250, 570, 350, 580, fill='antiquewhite1')    #On crée le widget raquette
    balle = canvas.create_oval(x, y, x + 10, y + 10, fill = 'antiquewhite1')        #On crée le widget balle

    win = canvas.create_text(1000, 1000, text = "You Win !", font = "Helvetica 50", fill='black')                       #On crée le widget "You win"
    gameover = canvas.create_text(1000, 1000, text = "Game Over",font= "Arial 30", fill='black')                        #On crée le widget "Game Over"
    restart = canvas.create_text(1000, 1000, text = "Appuyez sur R pour recommencer",font= "Arial 20", fill='black')    #On crée le widget "appuyez sur R pour recommencer"

    ligne = canvas.create_line(235, 370, 235, 450, width = 3, fill = 'antiquewhite1')   #On crée les widgets ligne pour dessiner le cube
    ligne = canvas.create_line(365, 370, 365, 450, width = 3, fill = 'antiquewhite1')
    ligne = canvas.create_line(235, 450, 300, 485, width = 3, fill = 'antiquewhite1')
    ligne = canvas.create_line(365, 450, 300, 485, width = 3, fill = 'antiquewhite1')
    ligne = canvas.create_line(235, 370, 300, 400, width = 3, fill = 'antiquewhite1')
    ligne = canvas.create_line(365, 370, 300, 400, width = 3, fill = 'antiquewhite1')
    ligne = canvas.create_line(235, 370, 300, 340, width = 3, fill = 'antiquewhite1')
    ligne = canvas.create_line(365, 370, 300, 340, width = 3, fill = 'antiquewhite1')
    ligne = canvas.create_line(300, 400, 300, 485, width = 3, fill = 'antiquewhite1')

    brique0  = canvas.create_rectangle(40, 100, 140, 125, fill = 'bisque4') #On crée les widgets pour chacune des briques
    brique1 = canvas.create_rectangle(180, 100, 280, 125, fill = 'bisque4')
    brique2 = canvas.create_rectangle(320, 100, 420, 125, fill = 'bisque4')
    brique3 = canvas.create_rectangle(460, 100, 560, 125, fill = 'bisque4')

    brique4 = canvas.create_rectangle(40, 200, 140, 225, fill = 'bisque3')
    brique5 = canvas.create_rectangle(180, 200, 280, 225, fill = 'bisque3')
    brique6 = canvas.create_rectangle(320, 200, 420, 225, fill = 'bisque3')
    brique7 = canvas.create_rectangle(460, 200, 560, 225, fill = 'bisque3')

    brique8 = canvas.create_rectangle(180, 300, 280, 325, fill = 'bisque2')
    brique9 = canvas.create_rectangle(320, 300, 420, 325, fill = 'bisque2')

    canvas.focus_set()                      #La fonction focus_set() est indispensable pour récupérer l'état d'une touche, mais on ne peut récuperer l'état que d'une seule tocuhe à la fois

    casse_brique.bind("<Key>", clavier)     #La fonction bind permet d’associer la fonction "clavier" à l'événement "Appuyer sur une touche du clavier"

    deplacement()                           #On execute la fonction déplacement à chaque tour de boucle

    casse_brique.mainloop()                 #Mainloop permet d'activer la boucle du programme, qui tournera en permanence

                                #PONG

def Pong():     #Fonction Pong

    global coords1, coords2, x, y, delta_x, delta_y, point_droite, point_gauche

    delta_x = 1     #variable de la balle en abscisse
    delta_y = -1    #variable de la balle en ordonnée
    x = 500         #position de la balle en abscisse
    y = 350         #position de la balle en ordonnée
    coords1 = (10,300)      #position de la raquette 1
    coords2 = (980,300)     #position de la raquette 2
    point_gauche = 0        #Score joueur 1
    point_droite = 0        #Score joueur 2

                                #Balle

    def deplacement():      #Fonction déplaçant la balle et gérant les rebonds

        global x, y, delta_x, delta_y, point_droite, point_gauche

        if y == 590:        #Rebond en bas
            delta_y = -1
        if y == 50:         #Rebond en haut
            delta_y = 1

        if x + 10 == 980 and y >= coords2[1] and y <= coords2[1]+25:        #Rebond sur chacune des raquettes
            delta_x = -1
            delta_y = -1
        if x + 10 == 980 and y >= coords2[1]+25 and y <= coords2[1]+75:
            delta_x = -1
        if x + 10 == 980 and y >= coords2[1]+75 and y <= coords2[1]+100:
            delta_x = -1
            delta_y = 1

        if x + 10 == 30 and y >= coords1[1] and y <= coords1[1]+25:
            delta_x = 1
            delta_y = -1
        if x + 10 == 30 and y >= coords1[1]+25 and y <= coords1[1]+75:
            delta_x = 1
        if x + 10 == 30 and y >= coords1[1]+75 and y <= coords1[1]+100:
            delta_x = 1
            delta_y = 1

        if x + 10 > 1000 and point_gauche == 2 :        #Si le joueur 2 rate la balle et que le joueur 1 est à 1 point de victoire
            canvas.coords(gameover, 500,300)            #On affiche "Joueur 1 gagne"
            canvas.coords(restart, 500,320)             #On affiche "Appuyer sur R pour recommencer"

        if x + 10 < 10 and point_droite == 2 :          #Même condition mais pour le joueur 1
            canvas.coords(gameover2, 500,300)
            canvas.coords(restart, 500,320)

        if x + 10 > 1000 and point_gauche == 0 :        #Si la balle sort de l'écran
            point_gauche += 1                           #On ajoute 1 au score du gagnant et on relance la balle de son côté
            delta_x = -1
            delta_y = -1
            x = 500
            y = 350
            canvas.coords(a0, 5000,300)
            canvas.coords(a1, 300,30)
            canvas.coords(a2, 5000,300)
            canvas.coords(a3, 5000,300)

        if x + 10 > 1000 and point_gauche == 1 :        #Si la balle sort de l'écran
            point_gauche += 1                           #On ajoute 1 au score du gagnant et on relance la balle de son côté
            delta_x = -1
            delta_y = -1
            x = 500
            y = 350
            canvas.coords(a0, 5000,300)
            canvas.coords(a1, 3000,30)
            canvas.coords(a2, 300,30)
            canvas.coords(a3, 5000,300)

        if x + 10 > 1000 and point_gauche == 2:         #Idem
            point_gauche += 1
            canvas.coords(a0, 5000,300)
            canvas.coords(a1, 5000,300)
            canvas.coords(a2, 5000,300)
            canvas.coords(a3, 300,30)

        if x + 10 < 10 and point_droite == 0 :          #Idem
            point_droite += 1
            delta_x = 1
            delta_y = -1
            x = 500
            y = 350
            canvas.coords(b0, 5000,300)
            canvas.coords(b1, 700,30)
            canvas.coords(b2, 5000,300)
            canvas.coords(b3, 5000,300)

        if x + 10 < 10 and point_droite == 1 :          #Idem
            point_droite += 1
            delta_x = 1
            delta_y = -1
            x = 500
            y = 350
            canvas.coords(b0, 5000,300)
            canvas.coords(b1, 3000,30)
            canvas.coords(b2, 700,30)
            canvas.coords(b3, 5000,300)

        if x + 10 < 10 and point_droite == 2:           #Idem
            point_droite += 1
            canvas.coords(b0, 5000,300)
            canvas.coords(b1, 5000,300)
            canvas.coords(b2, 5000,300)
            canvas.coords(b3, 700,30)

        x = x + delta_x                             #On ajoute à la coordonnée en abscisse la variation en abscisse (-1 ou 1)
        y = y + delta_y                             #On ajoute à la coordonnée en ordonnée la variation en ordonnée (-1 ou 1)
        pong.after(3,deplacement)                   #La fonction after execute toutes les x millisecondes la fonction déplacement
        canvas.coords(balle, x, y, x + 10, y + 10)  #On affiche la balle à ses nouvelles coordonnées

                                #Mouvements de la raquette

    def clavier(event):     #Fonction gérant le déplacement de la raquette avec les flèches, et la touche pour recommencer

        global coords1, coords2, delta_x, delta_y, x, y, point_droite, point_gauche

        touche = event.keysym   #variable récuperant l'état d'une touche

        if touche == "z" and coords1[1] != 50:      #Si on presse la touche Z et que la raquette n'est pas en haut de l'écran
            coords1 = (10, coords1[1] - 10)         #La raquette se déplace de -10 pixels en ordonnée

        if touche == "s" and coords1[1] != 500:     #Si on presse la touche S et que la raquette n'est pas en bas de l'écran
            coords1 = (10,coords1[1] + 10)          #La raquette se déplace de +10 pixels en ordonnée

        canvas.coords(raquette1, 10, coords1[1], 20, coords1[1] + 100)      #On affiche la raquette à ses nouvelles coordonnées

        if touche == "Up" and coords2[1] != 50:     #Idem pour la raquette 2, mais avec les flèches HAUT et BAS
            coords2 = (980, coords2[1] - 10)

        if touche == "Down" and coords2[1] != 500:
            coords2 = (980,coords2[1] + 10)

        canvas.coords(raquette2, 980, coords2[1], 990, coords2[1] + 100)

        if touche == "Escape" :     #Si on appuie sur échap, la fenêtre se ferme, on revient au menu
             pong.destroy()         #La fenêtre se ferme, on revient au menu

        if (touche == "r" and x + 10 > 1000 and point_gauche==3) or (touche == "r" and x + 10 > 1000 and point_droite==3) or (touche == "r" and x + 10 < 10 and point_droite==3) or (touche == "r" and x + 10 < 10 and point_gauche==3):
            #Si on appuie sur R, que la balle est sorti de l'écran, et qu'un des joueurs a gagné

            delta_x = 1     #On réinitialise chacun des coordonées et des variables
            delta_y = -1
            x = 500
            y = 350
            canvas.coords(gameover, 5000,300)
            canvas.coords(gameover2, 5000,300)
            canvas.coords(restart, 5000,300)

            point_droite = 0
            point_gauche = 0

            canvas.coords(a0, 300,30)
            canvas.coords(a1, 3003,30)
            canvas.coords(a2, 5000,300)
            canvas.coords(a3, 3003,30)

            canvas.coords(b0, 700,30)
            canvas.coords(b1, 7000,30)
            canvas.coords(b2, 5000,300)
            canvas.coords(b3, 5000,300)

                                #Création de la fenêtre

    pong = Tk()     #Création de la fenêtre Tkinter
    pong.title("Pong")
    pong.geometry("1000x600")

    canvas = Canvas(pong, width=1000, height=600, bg = "black")     #On crée le canvas
    canvas.pack()

    raquette1 = canvas.create_rectangle(10, 300, 20, 400, fill='RoyalBlue4')    #On crée le widget des 2 raquettes
    raquette2 = canvas.create_rectangle(980, 300, 990, 400, fill='firebrick2')

    gameover = canvas.create_text(5000, 300, text = "Game Over, Joueur 1 gagne", fill='white')      #On crée le widget pour afficher quel joueur a gagné et on affiche "Appuyer sur R pour recommencer"
    gameover2 = canvas.create_text(5000, 300, text = "Game Over, Joueur 2 gagne", fill='white')
    restart = canvas.create_text(5000, 300, text = "Appuyer sur R pour recommencer", fill='white')

    a0 = canvas.create_text(300, 30, text = "0", font="Arial 25", fill='white')         #On crée les widgets pour les différents points
    a1 = canvas.create_text(5000, 300, text = "1", font="Arial 25", fill='white')
    a2 = canvas.create_text(5000, 300, text = "2", font="Arial 25", fill='white')
    a3 = canvas.create_text(5000, 300, text = "3", font="Arial 25", fill='white')

    b0 = canvas.create_text(700, 30, text = "0", font="Arial 25", fill='white')
    b1 = canvas.create_text(5000, 300, text = "1", font="Arial 25", fill='white')
    b2 = canvas.create_text(5000, 300, text = "2", font="Arial 25", fill='white')
    b3 = canvas.create_text(5000, 300, text = "3", font="Arial 25", fill='white')

    ligne1 = canvas.create_line(500, 50, 500, 600, fill = 'white', dash=(5, 5))         #On crée la ligne verticale en pointillé
    ligne2 = canvas.create_line(0, 50, 1000, 50, fill = 'white')                        #On crée la ligne horizontale séparant les scores du jeu

    text1 = canvas.create_text(50, 25, text="Joueur 1", font="Arial 16", fill = 'white')    #On crée les widgets affichant le nom de chaque joueur
    text2 = canvas.create_text(950, 25, text="Joueur 2", font="Arial 16", fill = 'white')

    balle = canvas.create_oval(x, y, x + 10, y + 10, fill = 'white')        #On crée le widget de la balle

    canvas.focus_set()              #La fonction focus_set() est indispensable pour récupérer l'état d'une touche, mais on ne peut récuperer l'état que d'une seule tocuhe à la fois

    pong.bind("<Key>", clavier)     #La fonction bind permet d’associer la fonction "clavier" à l'événement "Appuyer sur une touche du clavier"

    deplacement()                   #On execute la fonction déplacement à chaque tour de boucle

    pong.mainloop()                 #Mainloop permet d'activer la boucle du programme, qui tournera en permanence

                                #MENU

menu = Tk()     #On cree la fenetre Tkinter du menu
menu.title("Menu")
menu.geometry("1024x599")

canvas = Canvas(menu, width=1024, height=599)   #On crée le canvas
canvas.pack()

canvas.create_text(512, 200, text="Casse brique", font="Arial 30", fill = 'gold')     #On crée le texte permettant d'acceder au casse-brique
canvas.create_text(512, 320, text="Pong", font="Arial 30", fill = 'white')            #On crée le texte permettant d'acceder au pong
canvas.create_text(512, 440, text="Quitter", font="Arial 30", fill = 'white')         #On crée le texte permettant de quitter le menu

select = 0      #variable permettant de savoir ou se situe le selecteur (select = 0 -> on a selectionné casse-brique ; select = 1 -> on a selectionné pong ; select = 2 -> on a selectionné quitter)

def menutouche(event):      #Fonction permettant de selectionner un mini-jeu

    global select

    touche = event.keysym       #variable récuperant l'état d'une touche

    if touche == "Up":      #Si on appuie sur la flèche HAUT

        if select == 1:     #Si select = 1

            canvas.create_text(512, 200, text="Casse brique", font="Arial 30", fill = 'gold')   #On affiche en surbrillance le casse brique ainsi slectionné
            canvas.create_text(512, 320, text="Pong", font="Arial 30", fill = 'white')
            canvas.create_text(512, 440, text="Quitter", font="Arial 30", fill = 'white')
            select = 0      #select = 0 -> on a selectionné casse-brique

        if select == 2:

            canvas.create_text(512, 200, text="Casse brique", font="Arial 30", fill = 'white')
            canvas.create_text(512, 320, text="Pong", font="Arial 30", fill = 'gold')           #On affiche en surbrillance le pong ainsi slectionné
            canvas.create_text(512, 440, text="Quitter", font="Arial 30", fill = 'white')
            select = 1      #select = 1 -> on a selectionné pong

    if touche == "Down":

        if select == 1:

            canvas.create_text(512, 200, text="Casse brique", font="Arial 30", fill = 'white')
            canvas.create_text(512, 320, text="Pong", font="Arial 30", fill = 'white')
            canvas.create_text(512, 440, text="Quitter", font="Arial 30", fill = 'gold')        #On affiche en surbrillance quitter ainsi slectionné
            select = 2      #select = 2 -> on a selectionné quitter

        if select == 0:

            canvas.create_text(512, 200, text="Casse brique", font="Arial 30", fill = 'white')
            canvas.create_text(512, 320, text="Pong", font="Arial 30", fill = 'gold')           #On affiche en surbrillance le pong ainsi slectionné
            canvas.create_text(512, 440, text="Quitter", font="Arial 30", fill = 'white')
            select = 1      #select = 1 -> on a selectionné pong

    if select == 0 and touche == "Return" :     #Si on selectionne le casse brique et qu'on valide avec entrée
        Casse_brique()                          #On lance la fonction Cassebrique()

    if select == 1 and touche == "Return" :     #Si on selectionne le pong et qu'on valide avec entrée
        Pong()                                  #On lance la fonction Pong()

    if select == 2 and touche == "Return" :     #Si on selectionne quitter et qu'on valide avec entrée
        menu.destroy()                          #On détruit la fenêtre -> Fin du programme

canvas.focus_set()                      #La fonction focus_set() est indispensable pour récupérer l'état d'une touche, mais on ne peut récuperer l'état que d'une seule tocuhe à la fois

menu.bind("<Key>", menutouche)          #La fonction bind permet d’associer la fonction "menutouche" à l'événement "Appuyer sur une touche du clavier"

menu.mainloop()                         #Mainloop permet d'activer la boucle du programme, qui tournera en permanence
