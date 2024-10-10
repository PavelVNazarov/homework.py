#
# Назаров ПВ
# module_14_2_old.py

import re

def extract_image_links(html_text):
    # Регулярное выражение для поиска ссылок на изображения
    pattern = r'<img\s+[^>]*src=[\'"]?(https?://[^\'" >]+?\.(?:jpg|jpeg|png|gif))[\'"]?'
    # Находим все совпадения по регулярному выражению
    image_links = re.findall(pattern, html_text, re.IGNORECASE)
    return image_links

sample_html = "<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> <img src='https://example.com/image3.gif'>"
image_links = extract_image_links(sample_html)

if image_links:
    for image_link in image_links:
        print(image_link)
else:
    print("Нет ссылок с картинками в HTML тексте.")