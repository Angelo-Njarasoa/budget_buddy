from backend.database import get_connection
from datetime import datetime

def add_transaction(user_id, amount, transaction_type, description, date):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO transactions (user_id, montant, type, description, date, categorie)
        VALUES (%s, %s, %s, %s, %s, 'salaire')
    """
    values = (user_id, amount, transaction_type, description, date)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


def make_transfer(sender_id, recipient_id, amount, description=""):

    date = datetime.now()
    desc = description or "Transfert"

    
    add_transaction(sender_id, amount + "envoyé" , "transfert", desc , date)

    
    add_transaction(recipient_id, amount +" reçu", "depot", desc, date)


def get_transactions_by_user(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM transactions WHERE user_id = %s ORDER BY date DESC", (user_id,))
    transactions = cursor.fetchall()
    cursor.close()
    conn.close()
    return transactions
