
class Compte:
    def __init__(self, identifiant: str, solde: float):
        if solde < 0:
            raise ValueError("Le solde initial ne peut pas être négatif")

        self._identifiant = identifiant
        self._solde = solde

    @property
    def identifiant(self):
        return self._identifiant

    @property
    def solde(self):
        return self._solde

    def deposer(self, montant: float):
        if montant <= 0:
            raise ValueError("Montant invalide")
        self._solde += montant

    def retirer(self, montant: float):
        if montant <= 0:
            raise ValueError("Montant invalide")
        if montant > self._solde:
            raise ValueError("Fonds insuffisants")
        self._solde -= montant