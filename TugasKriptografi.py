
def encrypt(plain_text, key):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, key):
    return encrypt(encrypted_text, -key)

def main():
    plain_text = input("Masukkan teks yang akan dienkripsi: ")
    key = int(input("Masukkan kunci enkripsi (bilangan bulat): "))

    encrypted_text = encrypt(plain_text, key)
    decrypted_text = decrypt(encrypted_text, key)

    print("Teks terenkripsi:", encrypted_text)
    print("Teks terdekripsi:", decrypted_text)

if __name__ == "__main__":
    main()
