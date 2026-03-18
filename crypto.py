# bcrypt module using the blowfish algorithm to perform the hash function
import bcrypt


def create_hash_salt(password):
    # encode the password into bytes
    salt = bcrypt.gensalt()
    password_bytes = password.encode('utf-8')
    password_hash = bcrypt.hashpw(password_bytes, salt=salt)
    return password_hash.decode()


def verify_password(hashed_password, input_password):
    input_password = input_password.encode('utf-8')
    if bcrypt.checkpw(input_password, hashed_password=hashed_password.encode('utf-8')):
        return True
    else:
        return False
    


    
