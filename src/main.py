import string
import secrets


class PasswordPolicy:
    def __init__(self, length=8, use_upper=True, use_lower=True, use_numbers=True, use_symbols=True):
        self.length = length
        self.use_upper = use_upper
        self.use_lower = use_lower
        self.use_numbers = use_numbers
        self.use_symbols = use_symbols


class PasswordGenerator:
    def __init__(self, policy : PasswordPolicy):
        self.policy = policy

    def generate(self):
        chars = ""

        if self.policy.use_upper:
            chars += string.ascii_uppercase
        if self.policy.use_lower:
            chars += string.ascii_lowercase
        if self.policy.use_numbers:
            chars += string.digits
        if self.policy.use_symbols:
            chars += string.punctuation

        if not chars:
            raise ValueError("At least one character must be provided")

        password = ""
        for i in range(self.policy.length):
            password += secrets.choice(chars)
        
        return password


class PasswordStrengthChecker:
    def check(self, password):
        score = 0

        length = len(password)

        if length >= 8:
            score += 1
        elif length >= 12:
            score += 2
        elif length >= 16:
            score += 3
        else:
            score += 4

        has_upper = False
        has_lower = False
        has_numbers = False
        has_symbols = False

        for char in password:
            if has_upper and has_lower and has_numbers and has_symbols:
                break

            if char in string.ascii_uppercase:
                has_upper = True
            elif char in string.ascii_lowercase:
                has_lower = True
            elif char in string.digits:
                has_numbers = True
            elif char in string.punctuation:
                has_symbols = True

        if has_upper:
            score += 1
        if has_lower:
            score += 1
        if has_numbers:
            score += 1
        if has_symbols:
            score += 1

        if score <= 3:
            strength = "Weak"
        elif score <= 6:
            strength = "Medium"
        else:
            strength = "Strong"

        return strength


def main():
    print("--- Password Generator ---")
    print("1. Generate a password")
    print("2. Check password strength")
    print("3. Exit")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                try:
                    length = int(input("Enter password length (8 minimum): "))

                    if length >= 8:
                        break
                    else:
                        print("Password length must be at least 8 characters.")
                except ValueError:
                    print("Please enter a valid number.")

            while True:
                use_upper = input("Use uppercase? (y/n): ")

                if use_upper == "y":
                    use_upper = True
                    break
                elif use_upper == "n":
                    use_upper = False
                    break
                else:
                    print("Please enter y or n.")

            while True:
                use_lower = input("Use lowercase? (y/n): ")

                if use_lower == "y":
                    use_lower = True
                    break
                elif use_lower == "n":
                    use_lower = False
                    break
                else:
                    print("Please enter y or n.")

            while True:
                use_numbers = input("Use numbers? (y/n): ")

                if use_numbers == "y":
                    use_numbers = True
                    break
                elif use_numbers == "n":
                    use_numbers = False
                    break
                else:
                    print("Please enter y or n.")

            while True:
                use_symbols = input("Use symbols? (y/n): ")

                if use_symbols == "y":
                    use_symbols = True
                    break
                elif use_symbols == "n":
                    use_symbols = False
                    break
                else:
                    print("Please enter y or n.")

            policy = PasswordPolicy(length, use_upper, use_lower, use_numbers, use_symbols)

            generator = PasswordGenerator(policy)

            final_password = generator.generate()

            print("Your password is: ", final_password)

        if choice == "2":
            password = input("Enter password: ")
            strength_checker = PasswordStrengthChecker()
            result = strength_checker.check(password)
            print("Strength: ", result)

        if choice == "3":
            exit()


if __name__ == "__main__":
    main()