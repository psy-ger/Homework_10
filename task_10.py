import re


def find_words(text: str, words: list) -> list:
    """
    Находит все слова из списка words в тексте (точное совпадение, регистр не важен).

    Args:
        text (str): Текст для поиска.
        words (list): Список слов для поиска.

    Returns:
        list: Список найденных слов.
    """
    pattern = r'\\b(' + '|'.join(map(re.escape, words)) + r')\\b'
    return re.findall(pattern, text, re.IGNORECASE)


def is_valid_date(date: str) -> bool:
    """
    Проверяет, соответствует ли дата формату DD.MM.YYYY.

    Args:
        date (str): Дата для проверки.

    Returns:
        bool: True, если дата валидна, иначе False.
    """
    pattern = r'^(0[1-9]|[12][0-9]|3[01])\\.(0[1-9]|1[0-2])\\.(\\d{4})$'
    return bool(re.match(pattern, date))


def find_ukrainian_words(text: str) -> list:
    """
    Находит все украинские слова (только буквы украинского алфавита).

    Args:
        text (str): Текст для поиска.

    Returns:
        list: Список найденных украинских слов.
    """
    pattern = r'\\b[А-Яа-яЇїІіЄєҐґ]+\\b'
    return re.findall(pattern, text)


# Приклади використання
if __name__ == "__main__":
    sample = "Сьогодні 28.09.2025. Привіт, world! #Python #2025"
    print(find_words(sample, ["world", "Привіт", "Python"]))
    print(is_valid_date("28.09.2025"))
    print(find_ukrainian_words(sample))
