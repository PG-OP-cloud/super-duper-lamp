import os
import base64
from cryptography.fernet import Fernet

# Retrieve and decode the secret key from environment variable
secret_key_base64 = os.getenv("SECRET_KEY")

if not secret_key_base64:
    print("❌ Error: SECRET_KEY is missing! Set it in GitHub Secrets.")
    exit(1)

key = base64.b64decode(secret_key_base64)

# Initialize Cipher
cipher = Fernet(key)

# Read the encrypted script
with open("my_script.enc", "rb") as file:
    encrypted_code = file.read()

# Decrypt the script
decrypted_code = cipher.decrypt(encrypted_code)

# Execute the decrypted code
exec(decrypted_code)
