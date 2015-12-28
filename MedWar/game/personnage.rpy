##### Classe #####
init python:
    class Personnage:
        character = None
        nom = ""
        
        def __init__(self,nom):
            self.character = Character(nom)
        #fin def
            
        def defCouleur(self,couleur):
            self.character.color = couleur
        #fin def
            
        def rendreDynamic(self):
            nd = "nomDynamic"
            nc =""
            condition = True
            it = 0
            
            while condition or it < 100:
                nc = nd+str(it)
                if nc in globals():
                    it+=1
                else:
                    globals()[nc] = "inconnu"
                    self.character.name = nc
                    self.character.dynamic = True
                    
                    condition = False
                #fin if
            #fin while
        #fin def
        
        def c(self):
            return self.character
        #fin def
        
        def changerNom(self):
            temp = self.character.name
            globals()[temp] = renpy.input("Quel est ton nom?")
        #end def
        
    #fin class

##### personnage principal #####
    pj = Personnage("pj")
    pj.defCouleur("#f00000")
    pj.rendreDynamic()

 #   nomDuJoueur = "joueur"
#    joueur = Character("nomDuJoueur",dynamic = False,color="#306090")
    #def ChangerNom(personnage):
    #    if personnage.dynamic:
    #        nomPersos[personnage.name] = renpy.input("Choisissez un nom")

##### Narrateurs #####