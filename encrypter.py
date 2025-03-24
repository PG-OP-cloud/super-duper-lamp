from cryptography.fernet import Fernet

# Load the secret key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Read the script to encrypt
with open("ai_coder.py", "rb") as file:
    original_code = file.read()

# Encrypt the script
encrypted_code = cipher.encrypt(original_code)

# Save encrypted script
with open("my_script.enc", "wb") as file:
    file.write(encrypted_code)

print("Script encrypted successfully!")
