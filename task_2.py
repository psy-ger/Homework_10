import re


def find_phone_numbers(text: str) -> list:
    """
    Находит все телефонные номера в тексте.

    Args:
        text (str): Текст для поиска номеров.

    Returns:
        list: Список найденных телефонных номеров.
    """
    pattern = r'(?:\(\d{3}\)\s?|\d{3}[.-]?)\d{3}[.-]?\d{4}'
    return re.findall(pattern, text)


# Example usage
if __name__ == "__main__":
    sample = "Call me at (123) 456-7890 or 123-456-7890, or 123.456.7890, or 1234567890."
    print(find_phone_numbers(sample))
