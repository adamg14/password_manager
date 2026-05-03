#!/bin/bash

# first check that the datbase path already exists
if [ -f "./password_manager.db" ]; then 
    read -p "The Database already exists.
    Recreate it? 
    This will delete all data. (y/n): " confirm
    if [ "$confirm" != "y" ]; then
        echo "Initialisation aborted."
        exit 0
    fi
    echo "Deleting the database file.
    All the data stored will be deleted"
    rm -rf ./password_manager
else
    touch ./password_manager.db
fi

DB_PATH="./password_manager.db"

# checking if sqlite3 is installed
if ! command -v sqlite3 &> /dev/null; then
    echo "sqlite3 is not installed. Install it with: brew install sqlite3"
    exit 1
fi


sqlite3 $DB_PATH <<EOF
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS vault;
DROP TABLE IF EXISTS entries;
CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL PRIMARY KEY,
    master_password_hash  TEXT NOT NULL,
    salt TEXT NOT NULL,
    created_at DATE TIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATE TIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS vault(
    vault_id TEXT NOT NULL PRIMARY KEY,
    vault_name TEXT NOT NULL,
    username TEXT NOT NULL,
    encrypted_key TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS entries (
    id TEXT NOT NULL PRIMARY KEY,
    vault_id TEXT NOT NULL REFERENCES vault(vault_id),
    type TEXT NOT NULL DEFAULT 'login',
    encrypted_data TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS access_granted (
    id TEXT NOT NULL PRIMARY KEY,
    vault_id TEXT NOT NULL REFERENCES vault(vault_id),
    username TEXT NOT NULL,
    access_give TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
EOF