from database import create_user, get_user_by_email
from transaction import add_transaction
import re


def inscrire_utilisateur(nom, prenom, email, password, solde_initial):
    # créer utilisateur
    create_user(nom, prenom, email, password)

    # récupérer utilisateur
    user = get_user_by_email(email)
    user_id = user["id"]

    # ajouter dépôt initial
    add_transaction(
        user_id=user_id,
        reference="INIT001",
        montant=solde_initial,
        type_transaction="depot",
        description="Solde initial",
        categorie="revenu",
        date="2026-03-20 10:00:00"
    )

    return user

if __name__ == "__main__":
    user = inscrire_utilisateur(
        "Alya",
        "Annabi",
        "alya2@test.com",
        "1234",
        500
    )

    print("Utilisateur créé :", user)



def verifier_mot_de_passe(password):
    if len(password) < 12:
        return False, "Le mot de passe doit contenir au moins 12 caractères"

    if not re.search(r"[A-Z]", password):
        return False, "Il faut au moins une majuscule"

    if not re.search(r"[0-9]", password):
        return False, "Il faut au moins un chiffre"

    if not re.search(r"[^A-Za-z0-9]", password):
        return False, "Il faut au moins un symbole"

    return True, "Mot de passe valide"