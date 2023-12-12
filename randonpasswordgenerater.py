import random
import string

def generate_password(l, capitals, smalls, numbers, special):
    capitals = string.ascii_uppercase
    smalls = string.ascii_lowercase
    numbers = string.digits
    specials = "@-_="

    a = 0
    password = ""

    if capitals:
        a += 26
        password += capitals

    if smalls:
        a += 26
        password += smalls

    if numbers:
        a += 10
        password += numbers

    if special:
        a += 4
        password += specials

    if a == 0:
        print("No character types selected. Password cannot be generated.")
        return

    print("Generated Password:", ''.join(random.choice(password) for _ in range(l)))

if __name__ == "__main__":
    l = int(input("Enter the length of the password: "))
    capitals = int(input("Include capitals (1 for yes, 0 for no): "))
    smalls = int(input("Include smalls (1 for yes, 0 for no): "))
    numbers = int(input("Include numbers (1 for yes, 0 for no): "))
    special = int(input("Include special characters (1 for yes, 0 for no): "))

    generate_password(l, capitals, smalls, numbers, special)
