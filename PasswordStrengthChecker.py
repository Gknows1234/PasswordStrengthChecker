
import re

WEAK_PASSWORDS = [
    "password", "123456", "qwerty", "123456789", "letmein",
    "welcome", "admin", "login", "iloveyou", "abc123"
]

def calculate_charset_size(pwd):
    size = 0

    if re.search(r"[a-z]", pwd):
        size += 26  

    if re.search(r"[A-Z]", pwd):
        size += 26  
    if re.search(r"[0-9]", pwd):
        size += 10  

    if re.search(r"[^A-Za-z0-9]", pwd):
        size += 32  

    return size

def estimate_crack_time(pwd):

    if pwd.lower() in WEAK_PASSWORDS:
        return "Instantly (common password detected!)"

    chars_per_pos = calculate_charset_size(pwd)

    pwd_len = len(pwd)

    combinations = chars_per_pos ** pwd_len

    attempts = combinations // 2

    time_in_seconds = attempts / 1_000_000_000

    if time_in_seconds < 1:
        return "Under 1 second"
    elif time_in_seconds < 60:
        return f"{time_in_seconds:.1f} seconds"
    elif time_in_seconds < 3600:
        return f"{time_in_seconds / 60:.1f} minutes"
    elif time_in_seconds < 86400:
        return f"{time_in_seconds / 3600:.1f} hours"
    elif time_in_seconds < 31536000:
        return f"{time_in_seconds / 86400:.1f} days"
    else:
        return f"{time_in_seconds / 31536000:.1f} years"

def evaluate_password(pwd):
    """Assess the strength of the provided password"""

    if not pwd:
        print("Please provide a password!")
        return

    print("\n--- Password Evaluation ---")
    print(f"Length: {len(pwd)} characters")
    print(f"Character set size: {calculate_charset_size(pwd)}")
    print(f"Estimated crack time: {estimate_crack_time(pwd)}")

    suggestions = []
    if len(pwd) < 8:
        suggestions.append("Increase length to at least 8 characters")
    if pwd.lower() in WEAK_PASSWORDS:
        suggestions.append("Avoid using well-known passwords")
    if not re.search(r"[a-z]", pwd):
        suggestions.append("Include lowercase letters (e.g., a, b, c)")
    if not re.search(r"[A-Z]", pwd):
        suggestions.append("Include uppercase letters (e.g., A, B, C)")
    if not re.search(r"[0-9]", pwd):
        suggestions.append("Include digits (e.g., 1, 2, 3)")
    if not re.search(r"[^A-Za-z0-9]", pwd):
        suggestions.append("Include special characters (e.g., !, @, #)")

    if suggestions:
        print("\nImprovement tips:")
        for tip in suggestions:
            print(f"  - {tip}")
    else:
        print("\nExcellent! This appears to be a robust password! 🚀")

if __name__ == "__main__":
    user_pwd = input("Input a password for evaluation: ")
    evaluate_password(user_pwd)
