from backend.database import create_user, get_user_by_email
from backend.transaction import add_transaction
import re


def register_user(nom, prenom, email, password, initial_balance):

    create_user(nom, prenom, email, password)

    user = get_user_by_email(email)
    user_id = user["id"]

    add_transaction(
        user_id=user_id,
        reference="INIT001",
        amount=initial_balance,
        transaction_type="depot",
        description="Initial balance",
        category="salaire",
        date="2026-03-20 10:00:00"
    )

    return user



def validate_password(password):
    if len(password) < 10:
        return False, "Minimum 10 caractères"

    if not re.search(r"[A-Z]", password):
        return False, "1 majuscule requise"

    if not re.search(r"[a-z]", password):
        return False, "1 minuscule requise"

    if not re.search(r"[0-9]", password):
        return False, "1 chiffre requis"

    if not re.search(r"[^A-Za-z0-9]", password):
        return False, "1 symbole requis"

    return True, "Mot de passe valide"