#
name = input("What is your name? ")

# 
age = input("What is your age in years? ")
age = int(age)
hourage = (age * 365 * 24)
mins = (hourage * 60)
seconds = (mins * 60)

#
print(name, "has been alive for:", age * 365, "Days")
print("Or:", hourage, "Hours")
print("Or:", hourage * 60, "Minutes")
print("Or:", hourage * 60 * 60, "Seconds")
print("You are:", age, "Years Old, Or", hourage, "Hours Old, Or", mins, "Minutes Old, Or", seconds, "Seconds Old!")
