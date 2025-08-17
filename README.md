# PasswordStrengthChecker
Password Strength Analyzer- evaluates password security against brute force attacks. Detects common weak passwords, calculates character set size (lowercase/uppercase/numbers/symbols), estimates crack time at 1 billion attempts/second, and provides personalized security recommendations in readable time format.



# Password Strength Analyzer

A Python tool that evaluates password security and estimates crack time using brute force attack modeling.

## Features

- **Common Password Detection**: Instantly identifies weak passwords from a predefined blacklist
- **Character Set Analysis**: Calculates password complexity based on character types used
- **Crack Time Estimation**: Estimates how long it would take to crack the password
- **Security Recommendations**: Provides personalized tips to improve password strength
- **Interactive Interface**: Easy-to-use command-line tool with formatted output

## How It Works

The analyzer uses the following methodology:

1. **Blacklist Check**: Compares against 10 common weak passwords
2. **Character Set Calculation**: 
   - Lowercase letters (a-z): +26 characters
   - Uppercase letters (A-Z): +26 characters
   - Numbers (0-9): +10 characters
   - Special characters: +32 characters
3. **Brute Force Modeling**: 
   - Assumes 1 billion attempts per second
   - Calculates total combinations: `charset_size^password_length`
   - Estimates average crack time (half of total combinations)

## Installation

No additional dependencies required - uses only Python standard library.

```bash
# Clone or download the script
python password_analyzer.py
```

## Usage

Run the script and enter a password when prompted:

```bash
python password_analyzer.py
```

### Example Output

```
Input a password for evaluation: MyP@ssw0rd123

--- Password Evaluation ---
Length: 13 characters
Character set size: 94
Estimated crack time: 2.4 years

Excellent! This appears to be a robust password! 🚀
```

### Weak Password Example

```
Input a password for evaluation: password

--- Password Evaluation ---
Length: 8 characters
Character set size: 26
Estimated crack time: Instantly (common password detected!)

Improvement tips:
  - Avoid using well-known passwords
  - Include uppercase letters (e.g., A, B, C)
  - Include digits (e.g., 1, 2, 3)
  - Include special characters (e.g., !, @, #)
```

## Security Recommendations

The tool provides specific suggestions based on password analysis:

- **Length**: Minimum 8 characters recommended
- **Character Diversity**: Use mix of uppercase, lowercase, numbers, and symbols
- **Avoid Common Passwords**: Don't use dictionary words or popular passwords
- **Complexity**: More character types = exponentially stronger security

## Limitations

- **Theoretical Model**: Based on pure brute force attacks only
- **Real-world Factors**: Doesn't account for dictionary attacks, rainbow tables, or social engineering
- **Hardware Assumptions**: Uses conservative 1 billion attempts/second rate
- **Educational Purpose**: Designed for learning, not production security assessment

## Common Weak Passwords Detected

- password
- 123456
- qwerty
- 123456789
- letmein
- welcome
- admin
- login
- iloveyou
- abc123

## Requirements

- Python 3.x
- Standard library modules: `re`

## License

Open source - feel free to modify and distribute.

## Contributing

Suggestions for improvement:
- Add more common passwords to blacklist
- Include dictionary word detection
- Implement password generation features
- Add GUI interface
