# Домашнее задание по теме "Логирование"
# Назаров ПВ
# tests_12_4_old.py

import requests
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Функция для проверки сайтов
def check_sites(site_list):
    for site in site_list:
        try:
            response = requests.get(site)
            if response.status_code == 200:
                log_site('success_responses.log', site)
            else:
                log_site('bad_responses.log', site)
        except requests.exceptions.RequestException:
            log_site('blocked_responses.log', site)

# Функция для логирования результатов
def log_site(filename, site):
    with open(filename, 'a') as f:
        f.write(f"{site}\n")

# Пример использования
if __name__ == "__main__":
    sites_to_check = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']
    check_sites(sites_to_check)
