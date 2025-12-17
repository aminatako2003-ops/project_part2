"""Module pour atome"""
class Atom():
    def __init__(self, name, num_electron,weight):

        self.name= name
        self.num_electron=num_electron
        self.weight=weight
        self.elec_config= self._elec_config()

    def __str__(self):
        return f"{self.name}({self.num_electron}{self.weight})"
    def __repr__(self):
        return f"{self.name}"
    def __eq__(self, value):
        return (self.name==value.name and
                self.num_electron==value.num_electron and
                self.weight==value.weight)
    def __hash__(self):
        """Rend l'objet Atom hashable pour pouvoir l'utiliser dans mol"""
        return hash((self.name, self.num_electron, self.weight))
    def _elec_config(self):
        """Calcule la configuration électronique par la règle de Klechkowski"""
        z= self.num_electron
        orbital_order=["1s","2s", "2p","3s", "3p","4s","3d", "4p","5s",
                    "4d", "5p","6s","4f", "5d", "6p","7s","5f", "6d", "7p"]
        orbital_capacity={"s": 2, "p": 6, "d": 10, "f": 14}
        reste=z
        config=[]
        for orb in orbital_order:
            l=orb[-1]
            n_elec=min(orbital_capacity[l], reste)
            if n_elec>0:
                config.append(f"{orb}{n_elec}")
                reste-=n_elec
            if reste <= 0:
                break
        return tuple(config)

#Dictionnaire contenant les propriétés des éléments chimiques
biosphere_elements = {
    "O": (8, 16),
    "C": (6, 12),
    "H": (1, 1),
    "N": (7, 14),
    "Ca": (20, 40),
    "P": (15, 31),
    "K": (19, 39),
    "S": (16, 32),
    "Na": (11, 23),
    "Cl": (17, 35.5),
    "Fe": (26, 56),
    "I": (53, 127),
    "F": (9, 19),
    "Co": (27, 59),
    "Mo": (42, 96)
}
#Création des instances Atom à partir du dictionnaire
biosphere_elements_instancies= [Atom(name, num_electron, weight) for name,
(num_electron, weight) in biosphere_elements.items()]
#Dictionnaire permettant d'accéder a un atome via son symbole
biosphere_elements_dict = {atom.name: atom for atom in biosphere_elements_instancies}
C = biosphere_elements_dict["C"]
H = biosphere_elements_dict["H"]
O = biosphere_elements_dict["O"]
Na = biosphere_elements_dict["Na"]
Cl = biosphere_elements_dict["Cl"]
F = biosphere_elements_dict["F"]
N = biosphere_elements_dict["N"]
P = biosphere_elements_dict["P"]
S = biosphere_elements_dict["S"]
