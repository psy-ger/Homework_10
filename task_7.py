import re


def extract_ipv4(text: str) -> list:
    pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    ips = re.findall(pattern, text)
    # Filter out invalid IPs (each octet <= 255)
    valid_ips = []
    for ip in ips:
        if all(0 <= int(octet) <= 255 for octet in ip.split('.')):
            valid_ips.append(ip)
    return valid_ips


# Example usage
if __name__ == "__main__":
    sample = "Valid: 192.168.1.1, Invalid: 999.999.999.999"
    print(extract_ipv4(sample))
