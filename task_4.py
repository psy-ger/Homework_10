import re


def format_date(date_str: str) -> str:
    """
    Преобразует дату из формата DD/MM/YYYY в формат YYYY-MM-DD.

    Args:
        date_str (str): Дата в формате DD/MM/YYYY.

    Returns:
        str: Дата в формате YYYY-MM-DD или None, если формат неверный.
    """
    pattern = r'(\d{2})/(\d{2})/(\d{4})'
    match = re.match(pattern, date_str)
    if match:
        day, month, year = match.groups()
        return f"{year}-{month}-{day}"
    return None


# Example usage
if __name__ == "__main__":
    print(format_date("28/09/2025"))
