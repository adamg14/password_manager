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