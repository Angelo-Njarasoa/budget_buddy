def filtrer_par_type(transactions, type_transaction):
    return [t for t in transactions if t["type"] == type_transaction]


def filtrer_par_categorie(transactions, categorie):
    return [t for t in transactions if t["categorie"] == categorie]


def filtrer_par_date(transactions, date):
    # format attendu : "2026-03-19"
    return [t for t in transactions if str(t["date"]).startswith(date)]


def filtrer_par_periode(transactions, date_debut, date_fin):
    resultat = []

    for t in transactions:
        date_transaction = str(t["date"])[:10]

        if date_debut <= date_transaction <= date_fin:
            resultat.append(t)

    return resultat


def trier_par_montant(transactions, ordre="croissant"):
    reverse = ordre == "decroissant"
    return sorted(transactions, key=lambda t: float(t["montant"]), reverse=reverse)



if __name__ == "__main__":
    from transaction import get_transactions_by_user

    user_id = 1
    transactions = get_transactions_by_user(user_id)

    print("Toutes :", transactions)

    print("\nFiltre type retrait :")
    print(filtrer_par_type(transactions, "retrait"))

    print("\nFiltre catégorie repas :")
    print(filtrer_par_categorie(transactions, "repas"))

    print("\nFiltre date 2026-03-19 :")
    print(filtrer_par_date(transactions, "2026-03-19"))

    print("\nFiltre période :")
    print(filtrer_par_periode(transactions, "2026-03-01", "2026-03-31"))

    print("\nTri montant décroissant :")
    print(trier_par_montant(transactions, "decroissant"))