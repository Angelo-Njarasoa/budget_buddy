from database import get_connection, get_user_by_email, create_user


def add_transaction(user_id, reference, montant, type_transaction, description, categorie, date):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO transactions (user_id, reference, montant, type, description, categorie, date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (user_id, reference, montant, type_transaction, description, categorie, date)

    cursor.execute(query, values)
    conn.commit()
    conn.close()


def get_transactions_by_user(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM transactions WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    transactions = cursor.fetchall()

    conn.close()
    return transactions
