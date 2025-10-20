import random
import string

def password_generator():
    try:
        print("WELCOME TO THE PASSWORD GENERATOR APP(^_^)")
        print("\nCarefully select your password elements:")
        length = input("How many characters: \t")
        if not length.isdigit() or int(length) <= 0:
            raise ValueError("❌ Password length must be a positive number.")
        length = int(length)
        param1 = input("Include letters? (y/n): ").strip().lower()
        param2 = input("Include numbers? (y/n): ").strip().lower()
        param3 = input("Include symbols? (y/n): ").strip().lower()

        if param1 not in ['y', 'n'] or param2 not in ['y', 'n'] or param3 not in ['y', 'n']:
            raise ValueError("❌ You must respond with 'y' or 'n' only.")
        if param1 == param2 == param3 == 'n':
            raise ValueError("❌ You must select at least one element type.")

        elements = ''
        if param1 == 'y':
            elements += string.ascii_letters
        if param2 == 'y':
            elements += string.digits
        if param3 == 'y':
            elements += string.punctuation

        password = ''.join(random.choice(elements) for _ in range(length))
        print(f"\n✅ Your generated password is:\n{password}")

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    password_generator()