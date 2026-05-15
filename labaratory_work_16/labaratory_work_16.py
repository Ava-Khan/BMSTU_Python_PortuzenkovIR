import re

with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Извлечение IP-адресов
ip_addresses = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", text)

# Извлечение методов и URL
methods_and_urls = re.findall(r"\"(GET|POST|PUT|DELETE) ([^\s\"]+)", text)
formatted_urls = [f"{method} {url}" for method, url in methods_and_urls]

# Извлечение кодов ошибок (кодов ответа HTTP)
error_codes = re.findall(r"\"\s(\d{3})\s", text)

# Вывод результатов поиска в консоль
print("=== РЕЗУЛЬТАТЫ ПОИСКА ===")
print(f"Найденные IP-адреса: {ip_addresses}")
print("-" * 50)
print(f"Найденные методы и URL: {formatted_urls}")
print("-" * 50)
print(f"Найденные коды ответов/ошибок: {error_codes}")
print("=========================")