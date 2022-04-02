age_str = input("How old are you?")
print(f"You typed in {age_str}.")
age_int = int(age_str)

if age_int >= 18:
    print("You are an adult")
else:
    print("You are not an adult")