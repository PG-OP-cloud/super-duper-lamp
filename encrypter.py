import os
import base64
from cryptography.fernet import Fernet

# Retrieve the secret key from GitHub Secrets (Environment Variable)
secret_key_base64 = os.getenv("SECRET_KEY")

if not secret_key_base64:
    print("❌ Error: SECRET_KEY is missing! Set it in GitHub Secrets.")
    exit(1)

# Decode the Base64 key
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
