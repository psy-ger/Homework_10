import re
from collections import Counter


def analyze_log_ip_stats(log_path: str) -> dict:
    """
    Аналізує лог-файл веб-сервера та повертає статистику запитів по IP-адресах.
    log_path: шлях до лог-файлу
    return: словник {ip: count}
    """
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    counter = Counter()
    with open(log_path, encoding='utf-8') as f:
        for line in f:
            ips = re.findall(ip_pattern, line)
            for ip in ips:
                if all(0 <= int(octet) <= 255 for octet in ip.split('.')):
                    counter[ip] += 1
    return dict(counter)


if __name__ == "__main__":
    # Пример: analyze_log_ip_stats('access.log')
    log_file = 'access.log'  # Замените на свой путь
    stats = analyze_log_ip_stats(log_file)
    for ip, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        print(f"{ip}: {count}")
