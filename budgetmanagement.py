def calculer_solde(transactions):
    solde = 0

    for t in transactions:
        if t["type"] == "depot":
            solde += float(t["montant"])
        else:
            solde -= float(t["montant"])

    return solde


def calculer_total_depots(transactions):
    total = 0
    for t in transactions:
        if t["type"] == "depot":
            total += float(t["montant"])
    return total


def calculer_total_retraits(transactions):
    total = 0
    for t in transactions:
        if t["type"] == "retrait":
            total += float(t["montant"])
    return total


def calculer_total_transferts(transactions):
    total = 0
    for t in transactions:
        if t["type"] == "transfert":
            total += float(t["montant"])
    return total


def detecter_decouvert(solde):
    return solde < 0


def generer_resume(transactions):
    solde = calculer_solde(transactions)
    total_depots = calculer_total_depots(transactions)
    total_retraits = calculer_total_retraits(transactions)
    total_transferts = calculer_total_transferts(transactions)

    return {
        "solde": solde,
        "total_depots": total_depots,
        "total_retraits": total_retraits,
        "total_transferts": total_transferts,
        "decouvert": detecter_decouvert(solde),
        "nombre_transactions": len(transactions)
    }

if __name__ == "__main__":
    from transaction import get_transactions_by_user

    user_id = 1
    transactions = get_transactions_by_user(user_id)

    print("Transactions :", transactions)
    print("Solde :", calculer_solde(transactions))
    print("Dépôts :", calculer_total_depots(transactions))
    print("Retraits :", calculer_total_retraits(transactions))
    print("Transferts :", calculer_total_transferts(transactions))
    print("Résumé :", generer_resume(transactions))