import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="budget_user",
        password="Budget123!",
        database="budget_buddy"
    )

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    conn.close()
    return user

def create_user(nom, prenom, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (nom, prenom, email, password)
        VALUES (%s, %s, %s, %s)
    """, (nom, prenom, email, password))

    conn.commit()
    conn.close()