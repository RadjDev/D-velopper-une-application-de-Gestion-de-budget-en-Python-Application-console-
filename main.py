''' application console de Gestion de budget
1) enregistrer ses dépenses
3) enregistrer ses revenus
3) voir l'écart qui est entre ses dépenses et ses revenus
4) une dépense peut etre dans une catégorie(Loyer, Manger, Transport etc...)
5) une revenus peut etre dans une catégorie(Salaire, Business etc...)
6) utilisez un dictionnaire 
'''

def AfficheRevenu():
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
    
def EcartDepnRe():
    global depnse01, revenu01
    for valeur in depnse01.values():   
            depnse01+=int(valeur) 
                                        
lancerProgram = "o"
# la liste des Dépenses et Revenus sont enrégistré dans des dictionnaire
ListeDepense = {"Loyer":"17000","Manger":"15000","Business":"50000","Transport":"5000"}
ListeRevenu = {"Salaire":"50000","Business":"50000","Cryptomonnais":"50000"}
#Depnse#revenu
NomdelaDepense="Nom de la Dépense"
NomdeRevenu="Nom du Revenu"
montant="Montant"
categorie="Catégorie"
revenu01={NomdeRevenu:"Entreprise A", montant:"100000",categorie:"Business"}
revenu02={NomdeRevenu:"Entreprise B", montant:"500000",categorie:"Business"}
depnse01={NomdelaDepense:"Achat de Bitcoin", montant:"208884",categorie:"Autre"}
depnse02={NomdelaDepense:"Achat de AVAX", montant:"574000",categorie:"Autre"}
#categorie depense
loyer="Loyer"
manger="Manger"
transport="Transport"
autredepense="Autre"
#categorie revenu
salaire="Salaire"
business="Business"
crypto="Cryptomonnaie"
autrerevenu="Autre"    
depnse01={}

grandeListedepen=[depnse01]
revenu01={}
grandeListeRevenu=[revenu01]
#revenu
NomduRevenu=""
montant=""
#des variables totalDepens et totalRevenu permettent de calculer l'ecart entre depenses et revenus
totalDepens=0
totalRevenu=0
# Une prémière boucle qui permet de maintenir l'execution repétitf des différents condition
while lancerProgram == "o":
    print("*********Bienvenu dans votre application console de Gestion de budget*********")
    affichmenue=("       ____________ MENU____________")
    print(affichmenue)
    print("Vous pouvez quitter à tout moment en appuyant sur q")
    bienvenu ="0"
    categoriedepen="0"
    while( bienvenu != "q" ):
        bienvenu = input(" Tapez 1 pour  enrégistrer des Dépenses \n Tapez 2 pour enrégistrer des Revenus \n Tapez 3 pour voir la liste des Revenus \n Tapez 4 pour voir la liste des Dépenses \n Tapez 5 pour voir l'écart qui est entre ses Dépenses et ses Revenus \n Tapez Q pour Quittez l'application\n")
        try :
            #depense
            if int(bienvenu) == 1:
                nomDepense=input("Quelle est le nom de la dépense ? \n")
                montantdepen=int(input("Quelle est le montant dépensé sur: \n" + nomDepense + "="))
                categoriedepen=(input("Quelle est la catégorie de la dépense ? \n Tapez A pour la catégorie Loyer \n Tapez B pour la catégorie Manger \n Tapez C pour la catégorie Transport \n Tapez D pour la catégorie Autre \n " ))
                if categoriedepen=="A":
                    depnse01[(categorie)]=[(loyer)]
                    grandeListedepen.append(depnse01)
                elif categoriedepen=="B":
                    depnse01[(categorie)]=[(manger)]
                    grandeListedepen.append(depnse01)   
                elif categoriedepen=="C":
                    depnse01[(categorie)]=[(transport)]
                    grandeListedepen.append(depnse01)    
                elif categoriedepen=="D":
                    depnse01[(categorie)]=[(autredepense)]
                    grandeListedepen.append(depnse01)                    
                else :
                    print("Veillez entré les options existente.")
                    print(affichmenue)
                    break
                             
                depnse01={NomdelaDepense:nomDepense, montant:montantdepen,categorie:categoriedepen}    
                grandeListedepen.append(depnse01)
                print("Vous avez enregistrer votre dépense {} avec succès".format(nomDepense))
                print(affichmenue) 
                
            #revenu    
            elif int(bienvenu)==2:
                nomRevenu=input("Quelle est le nom du Revenu ? \n")
                montantRevenu=int(input("Quelle est le montant du Revenu: \n" + nomRevenu + "="))
                categorieRevenu=(input("Quelle est la catégorie du Revenu ? \n Tapez A pour la catégorie Salaire \n Tapez B pour la catégorie Business \n Tapez C pour la catégorie Cryptomonnaie \n Tapez D pour la catégorie Autre \n " ))
                if categorieRevenu=="A":
                    revenu01[(categorie)]=[(salaire)]
                    grandeListeRevenu.append(revenu01)
                elif categorieRevenu=="B":
                    revenu01[(categorie)]=[(business)]
                    grandeListeRevenu.append(revenu01)   
                elif categorieRevenu=="C":
                    revenu01[(categorie)]=[(crypto)]
                    grandeListeRevenu.append(revenu01)    
                elif categorieRevenu=="D":
                    revenu01[(categorie)]=[(autrerevenu)]
                    grandeListeRevenu.append(revenu01)
                else :
                    print("Veillez entré les options existente.")
                    print(affichmenue)
                    break     
                revenu01={NomdeRevenu:nomRevenu, montant:montantRevenu,categorie:categorieRevenu}    
                grandeListeRevenu.append(revenu01)                
                print("Vous avez enregistrer votre Revenu {} avec succès".format(nomRevenu)) 
                print(affichmenue) 
                
            elif int(bienvenu)==5:
                EcartDepnRev()
                #ecart()
                print(affichmenue)     
                
            elif int(bienvenu)==3:
                AfficheRevenu()
                
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
