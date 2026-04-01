import datetime

def calculate_age():
    print("--- Age Counter ---")
    try:
        # Get user input
        birth_year = int(input("Enter your birth year (YYYY): "))
        birth_month = int(input("Enter your birth month (MM): "))
        birth_day = int(input("Enter your birth day (DD): "))

        # Get current date
        today = datetime.date.today()
        
        # Create birthday object for this year
        birthday = datetime.date(today.year, birth_month, birth_day)
        
        # Calculate age
        age = today.year - birth_year
        
        # Adjust if birthday hasn't happened yet this year
        if (today.month, today.day) < (birth_month, birth_day):
            age -= 1

        print("-" * 20)    
        print(f"\nYou are {age} years old.")
        
    except ValueError:
        print("Invalid input! Please enter numbers for date.")

if __name__ == "__main__":
    calculate_age()