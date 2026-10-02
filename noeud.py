import matplotlib.pyplot as plt

class Noeud:
    
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfants = []
        self.dict = {}

    def ajouter_noeud(self, noeud):
        self.enfants.append(noeud)

    def afficher_polonais(self):
        resultat = str(self.valeur)

        for enfant in self.enfants:
            resultat += " " + enfant.afficher_polonais()
        return(resultat)

    def evaluer(self, dict):
        self.dict = dict

        if isinstance(self.valeur,(int,float)):
            return float(self.valeur)

        if self.valeur == "*":
            res = 1
            for enfant in self.enfants:
                res *= enfant.evaluer(self.dict)
            return res

        if self.valeur == "+":
            res = 0
            for enfant in self.enfants:
                res += enfant.evaluer(self.dict)
            return res

        if self.valeur == "-":
            res = self.enfants[0].evaluer(self.dict)
            for enfant in self.enfants[1:]:
                res -= enfant.evaluer(self.dict)
            return res

        else :
            if self.valeur in self.dict:
                return self.dict[self.valeur]
            else:
                raise ValueError(f"La variable {self.valeur} n'est âs défini")

    def tracer(self, variable, valeurs):
        x = []

        for i in valeurs:
            dictionnaire = {variable: i}
            x.append(self.evaluer(dictionnaire))

        fonction = self.afficher_polonais()

        plt.plot(valeurs, x)
        plt.xlabel("Valeurs de x")
        plt.ylabel(fonction)
        plt.grid()
        plt.show()


