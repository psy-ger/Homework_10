import re


def remove_html_tags(text: str) -> str:
    """
    Удаляет все HTML-теги из текста.

    Args:
        text (str): Текст с HTML-тегами.

    Returns:
        str: Текст без HTML-тегов.
    """
    pattern = r'<[^>]+>'
    return re.sub(pattern, '', text)


# Example usage
if __name__ == "__main__":
    html = "<p>Hello <b>world</b>!</p>"
    print(remove_html_tags(html))
