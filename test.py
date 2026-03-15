from crypto import verify_password, create_hash_salt

def test_hashing_validation_v1():
    assert verify_password(
        create_hash_salt('password'),
        'password'
    ) == True


def test_hashing_validation_v2():
    assert verify_password(
        create_hash_salt('password'),
        'passwrd'
    ) == False
if __name__ == '__main__':
    print("1.1. Testing Hashing Validation - Valid Parameters")
    test_hashing_validation_v1()
    print("1.2. Testing Hashing Validation - Invalid Parameters")
    test_hashing_validation_v2()

