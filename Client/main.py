from Infrastructure.depot_memoire import DepotMemoire
from Application.service_compte import ServiceCompte

"""Point d'entrée de l'application pour tester les fonctionnalités du service de compte avec un dépôt en mémoire."""
repo = DepotMemoire()
service = ServiceCompte(repo)

client = service.creer_compte("client1", 1000)
print(f"Solde initial: {service.consulter_solde('client1')}")
service.deposer("client1", 500)
print(f"Solde après dépôt: {service.consulter_solde('client1')}")
service.retirer("client1", 200)
print(f"Solde après retrait: {service.consulter_solde('client1')}")
service.retirer("client1", 1500)  # Devrait lever une exception pour solde insuffisant

