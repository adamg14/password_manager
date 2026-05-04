# Password Manager                                             
## Zero-Knowledge, AES Encrypted, SHA-512 Hash Storage 

CLI-based password manager with zero-knowledge architecture, 
AES encryption, and SHA-512 hashing.                           

## Features                                                    
Zero-knowledge design — master password is never stored      

Database uses transactions to uphold ACID principals
- AES-encrypted vault storage                                  
- SHA-512 password hashing with salt                           
- Multiple vaults per user (e.g. Gmail, Work, Banking)         
- SQLite-backed local storage                                  

## Project Structure
- (`main.py`) = Entry point and the cli interface
- (`/querying`) = Database interaction. API of the interface.
- (`/testing`) = Testing script 
- (`/crypto`) = Cryptographic functionality of the project. Encryption, Decryption and Key Derivation Function    
py                                         
- (`requirements.txt`) = Python dependencies.

## Python 3.x                                                   
Dependencies listed in `requirements.txt`:                   
- sqlite3
- bcrypt
- sqlite3                                                        


## Installing the Python dependencies for this project using Pip
``shell
pip install -r requirements.txt                                
```                                                            
## Before running the Program:
Before running the program. Please run the so that the database is initialised (the database file and tables created) for you to use.
```shell
chmod +x ./init_script.sh
./init_script.sh
```
!! THIS BASH SCRIPT SHOULD BE EXECUTED ONCE ONLY BEFORE YOU USE THIS APPLICATION.

## Usage                                                       
```shell                                                       
python main.py                                                 
```                                                            

## From the home menu:                                            
1. **Login** — authenticate with your username and master password.                                                        
2. **Create Account** — register a new account                 
3. Once logged in you can:                                        
    - Change your master password                                  
    - Create named vaults                                          
    - View your vaults                                             
    - Add password entries to a vault                              
    - Plus many upcoming features

## Running Tests                                               
```shell                                                       
    chmod +x testing_script.sh
    ./testing_script.sh
```                                                                                                                                                 

## Flow of Project (Encryption  )
1. master password + salt
    - master password stored in user's local session (it is never stored in the database)
    - salt (which works in the key derivation function as an input - it's decoded value is stored in the users' database table)

2. KDF function
3. derived master key  (raw binary)
4. The derived master key (derived using the KDF with the salt and the raw master password as inputs) use it to decrypt the vault key from the database
5. decrypted vault key  (raw binary)
6. use it to encrypt the new password
7. encrypted password  (raw binary)
8. base64 encode it so it can be stored as text in SQLite
9. store in database

## Backwards Flow (Inverse/Decryption)

## Test Deployment 
[Test PyPi Deployment Link](https://test.pypi.org/project/adams-password-manager-cli-app/0.1.0/)