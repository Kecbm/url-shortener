# Our 62-character "alphabet"
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(ALPHABET)

def encode(num: int) -> str:
    """Converts an integer (database ID) into a Base62 string."""
    if num == 0:
        return ALPHABET[0]

    if num < BASE:
        return ALPHABET[num]

    return encode(num // BASE) + ALPHABET[num % BASE]

# For test in the terminal
if __name__ == "__main__":
    print("Test the base62 algorithm")
    print(f"ID 1     -> {encode(1)}")
    print(f"ID 10    -> {encode(10)}")
    print(f"ID 100   -> {encode(100)}")
    print(f"ID 9999  -> {encode(9999)}")
    print(f"ID 1000000 -> {encode(1000000)}")
