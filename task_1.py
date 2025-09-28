import re


def is_valid_email(email: str) -> bool:
    pattern = r'^(?![.])[A-Za-z0-9.]+(?<![.])@[A-Za-z0-9]+\.[A-Za-z]{2,6}$'
    return bool(re.match(pattern, email))


# Example usage
if __name__ == "__main__":
    emails = [
        "test.email@domain.com",
        "test@domain.net",
        ".test@domain.com",
        "test.@domain.com",
        "test@domain.c",
        "test@domain.company"
    ]
    for email in emails:
        print(f"{email}: {is_valid_email(email)}")
