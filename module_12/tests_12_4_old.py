# Домашнее задание по теме "Логирование"
# Назаров ПВ
# tests_12_4_old.py

import requests
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Лог файлы
success_log_file = 'success_responses.log'
bad_log_file = 'bad_responses.log'
blocked_log_file = 'blocked_responses.log'

def log_success(url, status_code):
    logging.info(f"'{url}', response - {status_code}")
    with open(success_log_file, 'a') as f:
        f.write(f"INFO: '{url}', response - {status_code}\n")

def log_bad(url, status_code):
    logging.warning(f"'{url}', response - {status_code}")
    with open(bad_log_file, 'a') as f:
        f.write(f"WARNING: '{url}', response - {status_code}\n")

def log_blocked(url):
    logging.error(f"{url}, NO CONNECTION")
    with open(blocked_log_file, 'a') as f:
        f.write(f"ERROR: '{url}', NO CONNECTION\n")

def check_sites(urls):
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                log_success(url, response.status_code)
            else:
                log_bad(url, response.status_code)
        except requests.ConnectionError:
            log_blocked(url)

if __name__ == "__main__":
    websites_to_check = ["https://www.youtube.com/", "https://wikipedia.org", "https://yahoo.com",
        "https://yandex.ru", "https://whatsapp.com", "https://amazon.com",
        "https://www.ozon.ru", "https://instagram.com", "https://twitter.com"]

    check_sites(websites_to_check)
