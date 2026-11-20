password = input("Enter your password: ")

mark = 0
has_upper = False
has_lower = False
has_digit = False
has_symbol = False
bad_password = False
has_repeated_char = False
if len(password) < 10:
    print("Password is too short")
else:
    mark += 2
    for char in password:
        password_count_char = password.count(char)
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if not char.isupper() and not char.islower() and not char.isdigit():
            has_symbol = True
        
if password_count_char > 6:
            print("Password is too weak because of repeated characters.")
            mark -= 5
            has_repeated_char = True

bad_password = False
if has_upper:
    mark += 1
if has_lower:
    mark += 1
if has_digit:
    mark += 1
if has_symbol:
    mark += 1
if "qwerty" in password.lower() or "123456" in password.lower() or "password" in password.lower():
    print("Password is too weak. Don't use easy combinations which can be easily guessed.")
    bad_password = True
    mark -= 7


if mark < 3:
    password_strength = "Weak"
elif mark == 3:
    password_strength = "Medium"
else:
    password_strength = "Strong"

if password_strength == "Weak" and bad_password == False and has_repeated_char == False:
    print("Your password is too Weak. Please use a combination of numbers, letters and special characters")
elif password_strength == "Medium" and bad_password == False and has_repeated_char == False:
    print("Your password is Medium. You can make it stronger or use it as it is but it is not recommended")
elif password_strength == "Strong" and bad_password == False and has_repeated_char == False:
    print("Your password is Strong") 