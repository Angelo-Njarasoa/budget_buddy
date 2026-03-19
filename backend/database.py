import mysql.connector

# 🔹 Connexion
def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="***",
        database="budget_buddy"
    )
    return conn


# 🔹 LOGIN
def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    conn.close()
    return user
def get_balance_by_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(montant) FROM transactions
        WHERE user_id = %s
    """, (user_id,))

    result = cursor.fetchone()
    conn.close()

    return result[0] if result[0] else 0

def login(email, password):
    user = get_user_by_email(email)

    if user and user["password"] == password:
        return user
    return None

# 🔹 INSCRIPTION
def create_user(nom, prenom, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (nom, prenom, email, password)
        VALUES (%s, %s, %s, %s)
    """, (nom, prenom, email, password))

    conn.commit()
    conn.close()