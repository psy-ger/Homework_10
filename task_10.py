import re


def find_words(text: str, words: list) -> list:
    """Знаходить усі слова з words у тексті (точний збіг, регістр не важливий)."""
    pattern = r'\\b(' + '|'.join(map(re.escape, words)) + r')\\b'
    return re.findall(pattern, text, re.IGNORECASE)


def is_valid_date(date: str) -> bool:
    """Перевіряє, чи дата у форматі DD.MM.YYYY"""
    pattern = r'^(0[1-9]|[12][0-9]|3[01])\\.(0[1-9]|1[0-2])\\.(\\d{4})$'
    return bool(re.match(pattern, date))


def find_ukrainian_words(text: str) -> list:
    """Знаходить усі українські слова (тільки літери українського алфавіту)."""
    pattern = r'\\b[А-Яа-яЇїІіЄєҐґ]+\\b'
    return re.findall(pattern, text)


# Приклади використання
if __name__ == "__main__":
    sample = "Сьогодні 28.09.2025. Привіт, world! #Python #2025"
    print(find_words(sample, ["world", "Привіт", "Python"]))
    print(is_valid_date("28.09.2025"))
    print(find_ukrainian_words(sample))
