from backend.database import get_connection
from datetime import datetime


def add_transaction(user_id, amount, transaction_type, description, date, category="salaire"):
    """Add a single transaction to the database"""
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO transactions (user_id, montant, type, description, date, categorie)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (user_id, amount, transaction_type, description, date, category)

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


def make_transfer(sender_id, recipient_id, amount, description=""):
    """Create TWO transaction lines for a transfer:
       - Sender is debited (transfert)
       - Recipient is credited (depot)"""
    date = datetime.now()
    desc = description or "Transfer"

    # Sender side - debit
    add_transaction(
        sender_id,
        amount,
        "transfert",
        desc + " - sent",
        date,
        category="salaire"          # 'salaire' is allowed in your ENUM
    )

    # Recipient side - credit
    add_transaction(
        recipient_id,
        amount,
        "depot",
        desc + " - received",
        date,
        category="salaire"          # 'salaire' is allowed in your ENUM
    )


def get_transactions_by_user(user_id):
    """Return all transactions for a specific user, ordered by date (newest first)"""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM transactions 
        WHERE user_id = %s 
        ORDER BY date DESC
    """, (user_id,))

    transactions = cursor.fetchall()
    cursor.close()
    conn.close()
    return transactions