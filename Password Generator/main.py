import random
lowers="abcdefghijklmnopqrstuvwxyz"
capitalized="ABCDEFGHIJKLMNOPQRSUVWXYZ"
numbers="1234567890"
symbols="!@#$%^&*()_+/*-<>?~|"
combined=lowers+capitalized+numbers+symbols
password_length=int(input("Enter password length: "))
password=""
for i in range(password_length):
    password=password + random.choice(combined)
print(password)