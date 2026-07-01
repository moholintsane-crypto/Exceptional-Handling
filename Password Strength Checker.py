import re

def check_password_strength(password):
    # Initialize score and feedback list
    score = 0
    feedback = []

    # 1. Check length
    if len(password) < 8:
        feedback.append("❌ Password must be at least 8 characters long.")
    else:
        score += 1

    # 2. Check for uppercase letters
    if not re.search(r"[A-Z]", password):
        feedback.append("❌ Password should contain at least one uppercase letter (A-Z).")
    else:
        score += 1

    # 3. Check for lowercase letters
    if not re.search(r"[a-z]", password):
        feedback.append("❌ Password should contain at least one lowercase letter (a-z).")
    else:
        score += 1

    # 4. Check for digits
    if not re.search(r"[0-9]", password):
        feedback.append("❌ Password should contain at least one number (0-9).")
    else:
        score += 1

    # Determine Strength based on score
    if score == 4:
        strength = "💪 Strong"
    elif score >= 2:
        strength = "⚠️ Moderate"
    else:
        strength = "🚨 Weak"

    return strength, feedback

def main():
    print("=== 🔐 Python Password Strength Checker ===")
    while True:
        user_password = input("\nEnter a password to test (or 'q' to quit): ")
        
        if user_password.lower() == 'q':
            print("Exiting checker. Goodbye!")
            break

        strength, feedback = check_password_strength(user_password)
        
        print(f"\nStrength: {strength}")
        if feedback:
            print("\nSuggestions to improve your password:")
            for item in feedback:
                print(item)

if __name__ == "__main__":
    main()
