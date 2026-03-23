def calculate_balance(transactions):
    balance = 0

    for t in transactions:
        amount = float(t["montant"])

        if t["type"] == "depot":
            balance += amount
        else:
            balance -= amount

    return balance


def total_deposits(transactions):
    return sum(float(t["montant"]) for t in transactions if t["type"] == "depot")


def total_withdrawals(transactions):
    return sum(float(t["montant"]) for t in transactions if t["type"] == "retrait")


def total_transfers(transactions):
    return sum(float(t["montant"]) for t in transactions if t["type"] == "transfert")


def is_overdrawn(balance):
    return balance < 0


def generate_summary(transactions):
    balance = calculate_balance(transactions)

    return {
        "balance": balance,
        "total_deposits": total_deposits(transactions),
        "total_withdrawals": total_withdrawals(transactions),
        "total_transfers": total_transfers(transactions),
        "overdrawn": is_overdrawn(balance),
        "transaction_count": len(transactions)
    }