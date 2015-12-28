#charge en mémoire les différents textes#

init python:
    import os
    os.chdir("C:/Users/chaos/OneDrive/Outils/Projet-RPG/textes")
    test = "intro.txt"
    test2 ="testecrit.txt"
    province_01 = "nom au hazard"
    nom_du_monde = "nom du monde"
    
    def lecteur():
        lecteur = open(test,"r")
        texte = lecteur.read()
        lecteur.close()
        return texte.decode("UTF-8")
    #fin def
    def ecrivain(st):
        lecteur = open(test2,"w")
        st.encode("UTF-8")
        lecteur.write(st)
        lecteur.close()
        return texte
    #fin def