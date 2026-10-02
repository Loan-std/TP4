from noeud import Noeud

n2 = Noeud(2)
y = Noeud("y")

add = Noeud("+")
add.ajouter_noeud(n2)
add.ajouter_noeud(y)

exp = Noeud("exp")
exp.ajouter_noeud(add)

print(exp.afficher_polonais())

variables = {
    "y": 3,
    "z": 6
}

print(add.evaluer(variables))

add.tracer("y", [0, 1, 2, 3, 4, 5])