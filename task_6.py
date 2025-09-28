import re


def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[@#$%&]', password):
        return False
    return True


# Example usage
if __name__ == "__main__":
    passwords = [
        "Password1@",
        "pass1@",
        "PASSWORD1@",
        "Password@",
        "Password1"
    ]
    for pwd in passwords:
        print(f"{pwd}: {is_strong_password(pwd)}")
