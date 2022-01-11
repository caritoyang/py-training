from cryptography.fernet import Fernet

# we will be encryting the below string.
password = "P4ssW0rd"

# generate a key for encryption and decryption
# You can use fernet to generate
# the key or use random key generator
key = Fernet.generate_key()

# Instance the Fernet class with the key
fernet = Fernet(key)

# to encrypt the string
encMessage = fernet.encrypt(password.encode())

print("original string: ", password)
print("encrypted string: ", encMessage)

# decrypt the encrypted string
decMessage = fernet.decrypt(encMessage).decode()


print("decrypted string: ", decMessage)
