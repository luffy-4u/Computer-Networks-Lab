# program for encryption

def encrypt(string,shift):
    cipher =""
    for char in string:
        if char == '':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65)% 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97)% 26 + 97)
    return cipher
text = input("Enter string:")
s = int(input("Enter shift number:"))
print("Original string:",text)
print("After encryption",encrypt(text,s))



#program for decryption

def decrypt(string,shift):
    cipher =""
    for char in string:
        if char == '':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) - shift - 65)% 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - shift - 97)% 26 + 97)
    return cipher
text = input("Enter string:")
s = int(input("Enter shift number:"))
print("Original string:",text)
print("After encryption",decrypt(text,s))
