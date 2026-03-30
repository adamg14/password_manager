CREATE TABLE IF NOT EXISTS entries (
    id TEXT NOT NULL PRIMARY KEY,
    vault_id TEXT NOT NULL REFERENCES vaults(id),
    type TEXT NOT NULL DEFAULT 'login',
    encrypted_data TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT now()
    updated_at TIMESTAMP DEFAULT now()
)