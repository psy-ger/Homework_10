import re


def extract_hashtags(text: str) -> list:
    pattern = r'#([A-Za-z0-9]+)'
    return re.findall(pattern, text)


# Example usage
if __name__ == "__main__":
    sample = "#hello world #Python3 #2025!"
    print(extract_hashtags(sample))
