import bcrypt
def hash_password(password: str):
    pw = bytes(password, "utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw, salt)
