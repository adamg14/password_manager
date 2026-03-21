import pytest
from crypto import verify_password, create_hash_salt
from db import db_cursor

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


@pytest.mark.parametrize(
        "password",
        [
            "pasword",
            "1111111111",
            ".JPsT=n1[73,"
        ]
)
def test_hash_random(password):
    assert create_hash_salt(password) != password


def test_db_connection():
    assert db_cursor is not None

@pytest.mark.parametrize(
    "table_name, expected",
    [
        ("password", True),
        ("user", True),
    ]
)

def test_user_table_exists(table_name, expected):
    query = db_cursor.execute(f"SELECT * FROM {table_name};")
    query_result = db_cursor.fetchone()
    assert query_result is not None
    

