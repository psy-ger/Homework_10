import re


def extract_hashtags(text: str) -> list:
    """
    Извлекает из текста все хештеги (#тег), состоящие из букв и цифр.

    Args:
        text (str): Текст для поиска хештегов.

    Returns:
        list: Список найденных хештегов.
    """
    pattern = r'#([A-Za-z0-9]+)'
    return re.findall(pattern, text)


# Example usage
if __name__ == "__main__":
    sample = "#hello world #Python3 #2025!"
    print(extract_hashtags(sample))
