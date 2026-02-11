# Password Generator & Strength Checker

A simple and secure Python project to **generate random secure passwords** and **check password strength**.

---

## Features

- Generate secure passwords using Python's `secrets` module  
- Customize password features:
  - Uppercase letters  
  - Lowercase letters  
  - Numbers  
  - Symbols  
- Check password strength based on:
  - Length  
  - Character diversity  
- User-friendly command-line interface (CLI)  
- Input validation to prevent errors

---

## Requirements

- Python 3.8+ (standard libraries: `string`, `secrets`)  
> No external packages are required.

---

## Usage

1. Run the main script:

```bash
python main.py
```

2. Menu options:

```
--- Password Generator ---
1. Generate a password
2. Check password strength
3. Exit
```

3. Choose an option:

- **1 → Generate a password**
  - Enter password length (minimum 8)  
  - Choose whether to include uppercase, lowercase, numbers, and symbols  
  - Generated secure password will be displayed  

- **2 → Check password strength**
  - Enter your password  
  - Output: Weak / Medium / Strong  

- **3 → Exit the program**

---

## Example

**Generate password:**

```
Enter your choice: 1
Enter password length (8 minimum): 12
Use uppercase? (y/n): y
Use lowercase? (y/n): y
Use numbers? (y/n): y
Use symbols? (y/n): n
Your password is: Abc123Xyz789
```

**Check password strength:**

```
Enter your choice: 2
Enter password: Abc123Xyz789
Strength: Medium
```

---

## License

This project is free to use for personal learning, practice, or educational purposes.
