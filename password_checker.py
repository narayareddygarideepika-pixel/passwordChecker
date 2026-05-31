from colorama import Fore, init
import re

# Start colorama
init()

password = input("Enter your password: ")

score = 0

# Length check
if len(password) >= 8:
    score += 1

# Uppercase check
if re.search("[A-Z]", password):
    score += 1

# Number check
if re.search("[0-9]", password):
    score += 1

# Special character check
if re.search("[@#$%^&*!]", password):
    score += 1

# Show score
print("Password Score:", score, "/4")

# Final result
if score == 4:
    print(Fore.GREEN + "Very Strong Password")
elif score >= 2:
    print(Fore.YELLOW + "Medium Password")
else:
    print(Fore.RED + "Weak Password")