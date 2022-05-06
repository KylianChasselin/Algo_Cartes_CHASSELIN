class Carte :
    def __init__ (self, name, mana, description) :
        self._nomCarte = name
        self._coutCarte = mana
        self._descriptionCarte = description
        self._surTerrain = False
        self._inMain = True
        self._inDefausse = False

class Mage :
    def __init__ (self, name, pv, manaFull, mana) :
        self._nomJ = name
        self._pvJ = pv
        self._manaTotalJ = manaFull
        self._manaActuelJ = mana
    def getNom1 (self) :
        return self._nomJ

class Main :
    def __init__ (self, listeCarte) :
        self._CarteMain = [listeCarte]
    def getListeCarte (self) :
        return self._CarteMain

class Defausse :
    def __init__ (self, listeDefause) :
        self._DefauseJoueur = listeDefause

class ZoneDeJeu :
    def __init__ (self, zoneMage, ZoneMage ) :
        self._ZoneMage = zoneMage
        self._ZoneMage = zoneMage

class Cristal(Carte) :
    def __init__ (self) :
        Carte.__init__ (self, "Cristal", 10, "Un cristal augmentant votre Mana Total de +1")

class Creature(Carte) :
    def __init__ (self, dgts, name, mana, description) :
        Carte.__init__ (self, "Creature", 10, "decription")
        self.degatsCreature = dgts
        self.nomCreature = name
        self.manaCreature = mana
        self.descriptionCreature = description

class Sort(Carte) :
    def __init__ (self, degatsSort) :
        Carte.__init__ (self, "Sort", 10, "Un sort qui inflige des dégâts")
        self.degatsSort = degatsSort


#-------------------------------------Main code-------------------------------------


print ("Bienvenue ! Affrontez d'autre mages grace a vos cartes, et remportez la victoire !")
print("Jouer vos cartez et attaquer celle de votre adversaire afin de lui retirer ses PV et gagner !")
Mage1 = Mage(input ("Mage 1, quel est vote nom ? "), 20, 15, 15)
Mage2 = Mage(input ("Mage 2, quel est vote nom ? "), 20, 15, 15)
tour = 0
victoire = False

print ("Mage 1 = ", Mage1._nom, " ! Et Mage 2 = ", Mage2._nom, " !")
print ("Vous allez jouer chacun votre tour en choisissant une carte parmis votre main que vous pourrez poser sur votre terrain ! Vous aurez 20 tours pour gagner, le vainqueur sera le joueur possedant le plus de point de vie !")

#while tour <20 or Joueur1._pv == 0 or Joueur2._pv == 0 :
print("C'est à ", Mage1._nom, " de jouer !")
print("Vous avez ", Mage2._manaActuel, " de Mana !" )
print ("Voici vos cartes disponibles : ")
carte1 = Creature(1, "Gobelin", 2, "Un gobelin voleur d'or. (2 MANA | 1 DEGATS)")
carte2 = Creature(2, "Troll", 3, "Un Troll des montagnes. (3 MANA | 2 DEGATS)")
carte3 = Creature(3, "Meute de Loups", 4, "une immense meute de loups prête a la chasse. (4 MANA | 3 DEGATS)")
carte4 = Creature(4, "Ent", 5, "Un geant qui vient tout droit de mère nature. (5 MANA | 4 DEGATS)")
carte5 = Creature(5, "Dragon", 3, "Une creature volante vivant pour le meurtre et la richesse. (6 MANA | 5 DEGATS)")
carte6 = Sort(5)
carte7 = Cristal()
listeCarteJoueur1 = ["Gobelin", "Troll", "Meute de Loups", "Ent", "Dragon", "Blast", "Cristal"]

print(listeCarteJoueur1)
choixCarteJoueur1 = input("Choisissez la carte à jouer : ")
if choixCarteJoueur1 in listeCarteJoueur1 :
    print(Mage1._nom, "joue : ", choixCarteJoueur1)
    if choixCarteJoueur1 == "Gobelin" :
        choixCarteJoueur1 == carte1
        print(carte1.creatureDescription)
        Mage1._manaActuel -= carte1.creatureMana
        print("Il vous reste ", Mage1._manaActuel, " de Mana " )

    elif choixCarteJoueur1 == "Troll" :
        choixCarteJoueur1 == carte2
        print(carte2.creatureDescription)
        Mage1._manaActuel -= carte2.creatureMana
        print("Il vous reste ", Mage1._manaActuel, " de Mana " )

    elif choixCarteJoueur1 == "Meute de Loups" :
        choixCarteJoueur1 == carte3
        print(carte3.creatureDescription)
        Mage1._manaActuel -= carte3.creatureMana
        print("Il vous reste ", Mage1._manaActuel, " de Mana " )
    
    elif choixCarteJoueur1 == "Ent" :
        choixCarteJoueur1 == carte4
        print(carte4.creatureDescription)
        Mage1._manaActuel -= carte4.creatureMana
        print("Il vous reste ", Mage1._manaActuel, " de Mana " )

    elif choixCarteJoueur1 == "Dragon" :
        choixCarteJoueur1 == carte5
        print(carte5.creatureDescription)
        Mage1._manaActuel -= carte5.creatureMana
        print("Il vous reste ", Mage1._manaActuel, " de Mana " )

    elif choixCarteJoueur1 == "Cristal" :
        choixCarteJoueur1 == carte7
        print (carte7._description)
        Mage1._manaActuel -= carte7._cout
        print("Il vous reste ", Mage1._manaActuel, " de Mana " )
        print("Vous avez joué un cristal ! +1 à votre mana. Mana total = ", Mage1._manaTotalJ += 1 , " !")

    elif choixCarteJoueur1 == "Sort" :
        choixCarteJoueur1 == carte6
        print(carte6._description)
        Mage1._manaActuel -= carte6._cout

# attack phase 

