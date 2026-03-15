import pytest
from crypto import verify_password, create_hash_salt

@pytest.mark.parametrize(
        "password, attempt, expected",
        [
            ("password", "password", True),
            ("password", "passwrd", False)
        ]
)
def test_password_verification(password, attempt, expected):
    hashed = create_hash_salt(password)
    assert verify_password(hashed_password=hashed,
    input_password=attempt) == expected

