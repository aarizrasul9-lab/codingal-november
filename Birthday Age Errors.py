from datetime import date

def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                print("Error: Age must be a positive number. Try again.")
                continue
            return age
        except ValueError:
            print("Error: Please enter a valid integer for age.")

def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name
        print("Error: Name cannot be empty. Try again.")

def calculate_age(birth_date):
    today = date.today()
    try:
        birthday = birth_date.replace(year=today.year)
    except ValueError:  # e.g., Feb 29 in non-leap year
        birthday = birth_date.replace(year=today.year, month=birth_date.month+1, day=1)
    if birthday > today:
        return today.year - birth_date.year - 1
    else:
        return today.year - birth_date.year

def categorize_age(age):
    if age < 13:
        return "Minor"
    elif age < 20:
        return "Youth"
    elif age < 60:
        return "Middle Age"
    else:
        return "Senior Citizen"

# Main program
while True:
    name = get_valid_name()
    age = get_valid_age()
    break  # Exit loop after valid inputs

print(f"{name}, you are {age} years old.")
print(categorize_age(age))

# Optional: calculate from birth date
try:
    birth_date = date(int(input("Enter birth year: )), int(input("Enter birth month: )), int(input("Enter birth day: )))
    calculated_age = calculate_age(birth_date)
    print(f"Calculated age from birth date: {calculated_age} years")
except ValueError:
    print("Error: Invalid date format. Please check your input.")
