# Name
name = input("What is your name? ")

# 
age = input("What is your age in years? ")
age = int(age)
hourage = (age * 365 * 24)

# Output
print(name, "has been alive for:", age * 365, "Days")
print("Or:", hourage, "Hours")
print("Or:", hourage * 60, "Minutes")
print("Or:", hourage * 60 * 60, "Seconds")
