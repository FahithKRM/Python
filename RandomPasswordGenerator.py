import random
import string

print("\nWelcome to the valided random password generator : )")
passwordLength = int(input("Enter the minimum length of password your need? :"))

# valided password inclued (numbers, letters both(lower & upper), special charactors)
letters = string.ascii_letters
numbers = string.digits
special = string.punctuation

password = letters + numbers + special
password = random.sample(password, passwordLength)
password = "".join(password)

print(f"\nMachine generated password : {password}")