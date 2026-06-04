
try:
    age = int(input("How old are you?"))

except ValueError:
    print("Sorry, your age isn't a number.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
