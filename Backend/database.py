import mysql.connector

# 🔹 Connexion
def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="je connais pas le code zut !",
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