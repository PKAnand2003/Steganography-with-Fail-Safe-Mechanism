import cv2
import os
import string

img = cv2.imread("Panda.jpg")
msg = input("Enter the Secret Message: ")
password = input("Enter a Password: ")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("EncryptedImage.jpg", img)
os.system("EncryptedImage.jpg")

message = ""
n = 0
m = 0
z = 0
print("You have 3 chances to unlock the message from the Encrypted image. Failed to do so, the Encrypted image will be deleted permanently.")
for j in range(3):
    pwd = input("Enter the password for Decryption: ")
    if password == pwd:
        for i in range(len(msg)):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        print("The Decryption message:", message)
        break
    else:
        if j==0:
            print("Invalid Password!!!")
            print("Your have last two chances to unlock the message from the Encrypted image")
            continue

        elif j==1:
            print("Invalid Password!!!")
            print("This is the last chance to unlock the message from the Encrypted image")
            continue
            
        elif j==2:
            print("Invalid Password!!!")
            
    print("You failed to unlock the message from the Encrypted image")
    os.remove("EncryptedImage.jpg")
    print("The Encrypted Image is deleted")
        
