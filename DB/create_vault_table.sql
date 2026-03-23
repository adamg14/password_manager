CREATE TABLE IF NOT EXISTS valut(
    id TEXT NOT NULL PRIMARY KEY,
    username TEXT NOT NULL,
    vault_id TEXT NOT NULL PRIMARY KEY,
    encrypted_key TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL
)