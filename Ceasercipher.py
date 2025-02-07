m = input("Message: ")
k = int(input("Key: "))
m = m.replace(" ", "")  # Remove spaces
m = m.lower()  # Convert the message to lowercase

letters = 'abcdefghijklmnopqrstuvwxyz1234567890~`-_+=}{[]\|:;<>,./!@#$%^&*()'

def Encrypt(m):
    e = ''
    for i in m:
        EX = letters[(letters.index(i) + k) % 26]
        e += EX
    return e

def Decrypt(m):
    e = ''
    for i in m:
        EX = letters[(letters.index(i) - k) % 26]
        e += EX
    return e

encrypted_message = Encrypt(m)
print("Encrypted:", encrypted_message)
decrypted_message = Decrypt(encrypted_message)
print("Decrypted:", decrypted_message)
