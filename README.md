# chempkg
Package Python pour modéliser des atomes, des molécules et des réactions chimiques simples.
## Installation
Créer un environnement virtuel puis installer le package en mode editable :
pip install -e .
### Utilisation
# Atom
from chempkg.atom import Atom, biosphere_elements_instancies
exemple:
carbon = Atom(name="C", num_electron=6, weight=12)
oxygen = Atom(name="O", num_electron=8, weight=16)
# Molecule
from chempkg.mol import Molecule
exemple:
ethanol = Molecule("C2OH6")
print(ethanol.atoms) renvoie {C: 2, O: 1, H: 6}
print(ethanol.weight) renvoie 46
# Réactions chimiques
from chempkg.reaction_utils import valid_reaction
exemple:
reactives = [("H2O", 2)]
products = [("H2", 2), ("O2", 1)]
print(valid_reaction(reactives, products)) renvoie True ou False
# Cinétiques
from chempkg.reaction_utils import kinetic_decomp
a_t = kinetic_decomp(a0=1.0, k=0.1, t=10, steps=50, figure_path="decomp.png")
