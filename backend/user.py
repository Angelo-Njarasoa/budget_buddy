from backend.database import get_user_by_email, email_exists, create_user
from backend.transaction import add_transaction
import re
import hashlib
import os


def register_user(nom, prenom, email, password, initial_balance):
    """Register a new user and create an initial deposit transaction"""
    create_user(nom, prenom, email, password)

    user = get_user_by_email(email)
    user_id = user["id"]

    add_transaction(
        user_id=user_id,
        reference="INIT001",
        amount=initial_balance,
        transaction_type="depot",
        description="Initial balance",
        category="salaire",
        date="2026-03-20 10:00:00"
    )

    return user


def validate_password(password):
    """Validate password according to security rules"""
    if len(password) < 10:
        return False, "Password must be at least 10 characters long"

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"

    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one number"

    if not re.search(r"[^A-Za-z0-9]", password):
        return False, "Password must contain at least one special character"

    return True, "Password is valid"


def is_valid_email(email: str) -> bool:
    """Check if the email format is valid"""
    pattern = r'^[a-zA-Z0-9._%+-]{2,}@[a-zA-Z0-9.-]{2,}\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_registration(nom: str, prenom: str, email: str, password: str):
    """Full registration validation (password + email + duplicate check)"""
    
    valid_pwd, msg_pwd = validate_password(password)
    if not valid_pwd:
        return False, msg_pwd

    if not is_valid_email(email):
        return False, "Invalid email format! Example: jean.dupont@gmail.com"

    if email_exists(email):
        return False, "This email is already used"

    return True, "Registration successful"


def hash_password(password: str) -> str:
    """Hash password with PBKDF2 + random salt (secure)"""
    salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt.hex() + ':' + hashed.hex()


def verify_password(plain_password: str, stored_hash: str) -> bool:
    """Verify password against stored hash"""
    try:
        salt_hex, hash_hex = stored_hash.split(':', 1)
        salt = bytes.fromhex(salt_hex)
        new_hash = hashlib.pbkdf2_hmac('sha256', plain_password.encode('utf-8'), salt, 100000)
        return new_hash.hex() == hash_hex
    except:
        return False