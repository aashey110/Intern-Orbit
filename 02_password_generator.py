import random
import string

password_length = int(input("Enter the length of the password: "))

password = ""

for i in range(password_length):
    password = password + random.choice(string.ascii_letters)

print("The generated password is: ")
print(password)