from Domain.compte import Compte


class ServiceCompte:
    """Couche de service gérant les opérations sur les comptes.

    Chaque méthode est documentée avec une docstring décrivant les
    paramètres, valeurs de retour et erreurs possibles. Cette organisation
    facilite la lecture du code et permet à des outils comme `help()` ou
    Sphinx de générer automatiquement de la documentation.
    """

    def __init__(self, depot):
        """Crée le service avec un dépôt donné.

        Args:
            depot: instance comportant les méthodes `save`, `get_by_id` et
                `exists` pour manipuler des objets `Compte`.
        """
        self._depot = depot

    def creer_compte(self, identifiant: str, solde: float):
        """Crée un compte et l'enregistre dans le dépôt.

        Args:
            identifiant: nom unique du compte.
            solde: montant initial (doit être >= 0).

        Returns:
            Le nouvel objet :class:`Domain.compte.Compte`.

        Raises:
            ValueError: si un compte avec le même identifiant existe déjà.
        """
        if self._depot.exists(identifiant):
            raise ValueError("Le compte existe déjà")

        compte = Compte(identifiant, solde)
        self._depot.save(compte)
        return compte

    def deposer(self, identifiant: str, montant: float):
        """Effectue un dépôt sur le compte donné.

        Args:
            identifiant: identifiant du compte destinataire.
            montant: somme à déposer (positive).

        Returns:
            Le compte mis à jour.

        Raises:
            ValueError: si le compte n'existe pas.
        """
        compte = self._depot.get_by_id(identifiant)
        if compte is None:
            raise ValueError("Compte introuvable")

        compte.deposer(montant)
        self._depot.save(compte)
        return compte

    def retirer(self, identifiant: str, montant: float):
        """Retire un montant du compte spécifié.

        Args:
            identifiant: identifiant du compte.
            montant: somme à retirer (positive et <= solde).

        Returns:
            Le compte mis à jour.

        Raises:
            ValueError: si le compte n'existe pas.
        """
        compte = self._depot.get_by_id(identifiant)
        if compte is None:
            raise ValueError("Compte introuvable")

        compte.retirer(montant)
        return compte

    def consulter_solde(self, identifiant: str) -> float:
        """Retourne le solde actuel d'un compte.

        Args:
            identifiant: identifiant du compte.

        Returns:
            Le solde du compte.

        Raises:
            ValueError: si le compte n'existe pas.
        """
        compte = self._depot.get_by_id(identifiant)
        if compte is None:
            raise ValueError("Compte introuvable")
        return compte.solde

    def run(self):
        """Exemple de méthode interactive ou de boucle de service.

        Cette méthode ne fait presque rien pour l'instant mais illustre où
        placer du code d'exécution "longue durée" (boucle, entrée utilisateur,
        etc.).
        """
        print("Service en cours d'exécution")
