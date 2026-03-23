import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="gros bifton ",
        database="budget_buddy"
    )

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def email_exists(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
    exists = cursor.fetchone() is not None
    cursor.close()
    conn.close()
    return exists

def login(email, password):
    from backend.user import verify_password
    user = get_user_by_email(email)
    if not user:
        return None
    if verify_password(password, user["password"]):
        return user
    return None

def create_user(nom, prenom, email, password):
    from backend.user import validate_registration, hash_password
    
    valid, msg = validate_registration(nom.strip(), prenom.strip(), email.strip(), password)
    if not valid:
        print(f" {msg}")
        return False

    hashed_password = hash_password(password)

    conn = get_connection()
    if not conn:
        return False

    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (nom, prenom, email, password)
            VALUES (%s, %s, %s, %s)
        """, (nom.strip(), prenom.strip(), email.strip(), hashed_password))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def get_balance_by_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(montant) FROM transactions WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result and result[0] else 0
