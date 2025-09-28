import re


def extract_urls(text: str) -> list:
    """
    Извлекает все URL из текста.

    Args:
        text (str): Текст для поиска URL.

    Returns:
        list: Список найденных URL.
    """
    pattern = r'https?://[\w.-]+(?:/[\w./?%&=-]*)?'
    return re.findall(pattern, text)


# Example usage
if __name__ == "__main__":
    sample = "Visit https://example.com and http://test.net/page?query=1"
    print(extract_urls(sample))
