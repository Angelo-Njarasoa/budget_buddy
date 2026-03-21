from transaction import get_transactions_by_user
from budgetmanagement import calculer_solde

user_id = 1

transactions = get_transactions_by_user(user_id)

print("Transactions :", transactions)
print("Solde :", calculer_solde(transactions))