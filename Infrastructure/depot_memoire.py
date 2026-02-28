from Domain.compte_sauvegarde import CompteSauvegarde

class DepotMemoire(CompteSauvegarde):
    def __init__(self):
        self._comptes = {}

    def save(self, compte):
        self._comptes[compte.identifiant] = compte

    def get_by_id(self, identifiant):

        return self._comptes.get(identifiant, None)


    def exists(self, identifiant):
        return identifiant in self._comptes
