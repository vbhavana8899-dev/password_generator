import secrets
import string


def generate_letters_only(length):
    pool = string.ascii_letters
    return ''.join(secrets.choice(pool) for _ in range(length))

def generate_alphanumeric(length):
    pool = string.ascii_letters + string.digits
    return ''.join(secrets.choice(pool) for _ in range(length))

def generate_full(length):
    pool = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(pool) for _ in range(length))

def generate_pin(length):
    pool = string.digits
    return ''.join(secrets.choice(pool) for _ in range(length))


def password_generator():
    print("Simple Password Generator")
    print("-------------------------")
    print("Types: 1) Letters only  2) Alphanumeric  3) Full (with symbols)  4) PIN (digits only)")

    while True:
        try:
            ptype = input("\nEnter password type (1, 2, 3, 4): ").strip()
            length = int(input("Enter password length: "))

            if length < 4:
                print("Error: Length must be at least 4.")
                continue

            if ptype == "1":
                result = generate_letters_only(length)
            elif ptype == "2":
                result = generate_alphanumeric(length)
            elif ptype == "3":
                result = generate_full(length)
            elif ptype == "4":
                result = generate_pin(length)
            else:
                print("Invalid type. Please choose 1, 2, 3, or 4.")
                continue

            print(f"Generated Password: {result}")

        except ValueError as e:
            print(f"Error: {e}")

        again = input("\nGenerate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    password_generator()
