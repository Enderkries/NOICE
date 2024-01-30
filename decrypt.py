#import Modules

import os
import base64
from cryptography.fernet import Fernet

#Find files
files = []

for file in os.listdir():
        if file == "encrypt.py" or file == "malware.py" or file == "grabber.py"  or file == "key.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)
                
# Get the encoded key variable
encoded_secret_key = input("Enter the key: ")

# Decode the key
secret_key = base64.b64decode(encoded_secret_key)

print(files)
        
#Decrypt files
for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        decrypted_contents = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(decrypted_contents)
            
print("All ur files have been decrypted\nYay!")
