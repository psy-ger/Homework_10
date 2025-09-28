import re


def remove_html_tags(text: str) -> str:
    pattern = r'<[^>]+>'
    return re.sub(pattern, '', text)


# Example usage
if __name__ == "__main__":
    html = "<p>Hello <b>world</b>!</p>"
    print(remove_html_tags(html))
