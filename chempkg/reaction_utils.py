import math

import matplotlib.pyplot as plt

from chempkg.mol import Molecule

def valid_reaction(reactives,products):
    """Vérifie si une reaction chimique est valide"""
    dict_reactives={}
    dict_products={}
    for j in products:
        for key,value in (Molecule(j[0]).atoms).items():
            total=value*int(j[1])
            dict_products[key]=dict_products.get(key,0)+total
    for i in reactives:
        for key,value in (Molecule(i[0]).atoms).items():
            total=value*int(i[1])
            dict_reactives[key]=dict_reactives.get(key,0)+total
    if dict_reactives==dict_products:
        return True
    return False
def  kinetic_decomp(a0, k,t,steps=10,figure_path=None):
    a_t=[]
    t=[i*t/steps for i in range (steps)]
    for j in (t):
        a_t.append((a0*math.exp(-k*j)))
    if figure_path:
        plt.plot(t, a_t)
        plt.title("Evolution [A](t)")
        plt.xlabel("temps(en seconde)")
        plt.ylabel("[A](t)mol.L-1")
        plt.savefig(figure_path)
        plt.show()
    return a_t
