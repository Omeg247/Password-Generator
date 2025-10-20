import random
import string

def leet_transform(word):
    #Convert letters to similar-looking numbers(leet style)
    leet_map = str.maketrans({
        'a': '4', 'A': '4',
        'e': '3', 'E': '3',
        'i': '1', 'I': '1',
        'o': '0', 'O': '0',
        's': '5', 'S': '5',
        't': '7', 'T': '7'
    })
    return word.translate(leet_map)

def password_generator():
    try:
        print("WELCOME TO THE PASSWORD GENERATOR APP(^_^)")
        print("\nCreate custom password🔤")
        base = input("Enter base word: ").strip()

        if not base:
            raise ValueError("❌ You must enter at least one word.")

        param1 = input("Include numbers? (y/n): ").strip().lower()
        param2 = input("Include symbols? (y/n): ").strip().lower()

        if param1 not in ['y', 'n'] or param2 not in ['y', 'n']:
            raise ValueError("❌ You must respond with 'y' or 'n' only.")

        #variations to transform base word
        variations = [
            base.lower(),
            base.upper(),
            base.capitalize(),
            leet_transform(base),
        ]

        #Pick one of the variations randomly
        chosen_base = random.choice(variations)

        #Add optional numbers/symbols before or after
        prefix, suffix = '', ''

        if param1 == 'y':
            digits = ''.join(random.choices(string.digits, k=random.randint(2, 4)))
            if random.choice([True, False]):
                prefix += digits
            else:
                suffix += digits

        if param2 == 'y':
            symbols = ''.join(random.choices(string.punctuation, k=random.randint(1, 3)))
            if random.choice([True, False]):
                prefix = symbols + prefix
            else:
                suffix += symbols

        final_password = f"{prefix}{chosen_base}{suffix}"

        print(f"\n✅ Your generated password is:\n{final_password}")

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    password_generator()