''' application console de Gestion de budget
1) enregistrer ses dépenses
3) enregistrer ses revenus
3) voir l'écart qui est entre ses dépenses et ses revenus
4) une dépense peut etre dans une catégorie(Loyer, Manger, Transport etc...)
5) une revenus peut etre dans une catégorie(Salaire, Business etc...)

'''

def AfficheRevenur():
            for cle,valeur in ListeRevenu.items(): 
                print(cle +"="+valeur) 
            print(affichmenue)
            
def AfficherDepense():
            for cle,valeur in ListeDepense.items(): 
                print(cle +"="+valeur)
            print(affichmenue) 
#Fonction permettant de calculer l'écart qui est entre ses dépenses et ses revenus                     
def EcartDepnRev():
    global totalDepens, totalRevenu
    for valeur in ListeDepense.values():   
            totalDepens+=int(valeur) 
    print("Total des Dépenses est {}".format(totalDepens)) 
    for valeur in ListeRevenu.values():
            totalRevenu+=int(valeur)
    print("Total des Revenus est {}".format(totalRevenu))
    ecart = totalRevenu-totalDepens 
    print("L'écart qui est entre ses Dépenses et ses Revenus est {}".format(ecart))       
        
                  
                           
lancerProgram = "o"
# la liste des Dépenses et Revenus sont enrégistré dans des dictionnaire
ListeDepense = {"Loyer":"17000","Manger":"15000","Business":"50000","Transport":"5000"}
ListeRevenu = {"Salaire":"50000","Business":"50000","Cryptomonnais":"50000"}
#des variables totalDepens et totalRevenu permettent de calculer l'ecart entre depenses et revenus
totalDepens=0
totalRevenu=0
# Une prémière boucle qui permet de maintenir l'execution repétitf des différents condition
while lancerProgram == "o":
    print("*********Bienvenu dans votre application console de Gestion de budget*********")
    affichmenue=("       ____________ MENU____________")
    print(affichmenue)
    print("Vous pouvez quitter à tout moment en appuyant sur 0")
    bienvenu ="0"
    while( bienvenu != "q" ):
        bienvenu = input(" Tapez 1 pour  enrégistrer des Dépenses \n Tapez 2 pour enrégistrer des Revenus \n Tapez 3 pour voir la liste des Dépenses \n Tapez 4 pour voir la liste des Revenus \n Tapez 5 pour voir l'écart qui est entre ses Dépenses et ses Revenus  \n Tapez Q pour Quittez l'application\n")
        try :
            if int(bienvenu) == 1:
                nomDepense=input("Quelle est le nom de la dépense ? \n")
                montantdepen=int(input("Quelle est le montant dépensé sur: \n" + nomDepense + "="))
                ListeDepense[(nomDepense)]=(montantdepen)
                print("Vous avez enregistrer votre dépense {} avec succès".format(nomDepense))
                print(affichmenue) 
                
            elif int(bienvenu)==2:
                nomDepense=input("Quelle est le nom du Revenu ? \n")
                montantdepen=int(input("Quelle est le montant du Revenu: \n" + nomDepense + "="))
                ListeRevenu[(nomDepense)]=(montantdepen)
                print("Vous avez enregistrer votre Revenu {} avec succès".format(nomDepense)) 
                print(affichmenue) 
                
            elif int(bienvenu)==5:
                EcartDepnRev()
                print(affichmenue)     
                
            elif int(bienvenu)==3:
                AfficheRevenur()
                
            elif int(bienvenu)==4:
                AfficherDepense()
                 
            else :
                print("Vous n'avez ni entré une option existente  ni appuyé sur la touche Q.")
                print(affichmenue)         
                            
        except:
            if str(bienvenu).lower()== "q":
                break
            else :
                print("Vous n'avez ni entré une option existente  ni appuyé sur la touche Q.")
                print(affichmenue)
                
    lancerProgram = input("Voulez-vous recommencer ? o/n \n").lower()
 
print("Vous avez quitté l'application")
