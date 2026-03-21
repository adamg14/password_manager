CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL PRIMARY KEY,
    master_password_hash  TEXT NOT NULL
    salt TEXT NOT NULL
    created_at DATE TIME NOT NULL
    updated_at DATE TIME NOT NULL
)