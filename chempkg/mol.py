from chempkg.atom import biosphere_elements_instancies
class Molecule():
    def __init__(self,formula):
    #Vérifie si formula est une chaîne de caractères ou un molecule(j'avais des erreurs sinon)
        if isinstance(formula, str):
            self.formula=formula.strip() #Supprime les espaces
        elif isinstance(formula, Molecule):
            self.formula=formula.formula  #on le prend si cest deja une molecule
        else:
            raise TypeError("Formula doit etre un str")
        self.atoms= self._atoms()
        self.weight=self._weight()
    def __str__(self):
        return f"Molecule({self.formula})"
    def __repr__(self):
        return f"{self.formula}"
    def __eq__(self, value):
        return self.formula==value.formula
    def _atoms(self):
        """Retourne un dictionnaire {Atom: nombre}"""
        atom_dict={}
        i=0
        while i<len(self.formula):
            symbole=self.formula[i] #Premier caractere du symbole de l'atome
            # Vérifie s'il y a un deuxième caractère
            if i+1<len(self.formula) and self.formula[i+1].islower():
                symbole+=self.formula[i+1]
                i+=1
            symbole=symbole[0].upper()+symbole[1:].lower()
            symbole = symbole.strip()
            i +=1
            number_str= str()
            #calculer le nombre d'atomes
            while i < len(self.formula) and self.formula[i].isdigit():
                number_str += self.formula[i]
                i+=1
            if number_str:
                number = int(number_str)
            else:
                number=1
            atom_instance=None       
            for atom in biosphere_elements_instancies:
                if atom.name.strip()==symbole.strip():
                    atom_instance=atom
                    break
            #Ajoute l'atome au dictionnaire
            if atom_instance in atom_dict:
                atom_dict[atom_instance] += number
            elif atom_instance is None:
                raise ValueError(f"Unknown atom symbol: {symbole}")
            else:
                atom_dict[atom_instance]=number
        return atom_dict
    def _weight(self):
        """Retourne la masse molaire de la molécule"""
        weight=0
        for atom,number in self.atoms.items():
            weight += float(atom.weight)*number
        return float(weight)
