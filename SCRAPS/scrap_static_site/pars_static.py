# Устанавливаем необходимые библиотеки
import random
import requests
from bs4 import BeautifulSoup
import json
import csv
# добавляем ссылку основной страницы сайта
url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
# Добавляем параметры браузера для запросов
headers = {
    "accept": "*/*",
    "user-agent": ""
}
# Заходим на сайт и копируем код страницы
req = requests.get(url, headers=headers)
src = req.text
#print(src)

with open("index.html", "w") as file:
   file.write(src)

# Открываем html и записываем все необходимые ссылки со значениями в json
with open("index.html") as file:
   src = file.read()

soup = BeautifulSoup(src, "lxml")
all_prod_hrefs = soup.find_all(class_='mzr-tc-group-item-href')

all_cetegor_dict = {}
for item in all_prod_hrefs:
item_text = item.text
item_href = 'https://health-diet.ru' + item.get('href')
#print(f"{item_text}-{item_href}")

all_cetegor_dict[item_text] = item_href
with open('ll_cetegor_dict.json', 'w') as file:
json.dump(all_cetegor_dict, file, indent=4, ensure_ascii=False)


with open("ll_cetegor_dict.json") as file:
    all_categpries = json.load(file)

# print(all_categpries)
# Собираем данные с каждой страницы и записываем в таблицы
iteration_count = int(len(all_categpries)) - 1
count = 0
for category_name, category_href in all_categpries.items():
    rep = [",", " ", "-", "'"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")
    # print(category_name)

    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f"data/{count}_{category_name}.html", "w") as file:
        file.write(src)
    with open(f"data/{count}_{category_name}.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    # проверка страницы на наличие таблицы
    alert_block = soup.find(class_="uk-alert-danger")
    if alert_block is not None:
        continue

    # Собираем заголовки таблицы
    table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
    # print(table_head)
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text

    with open(f"data/{count}_{category_name}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )
    # Собираем данные продуктов
    products_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")
    product_info = []
    for item in products_data:
        products_tds = item.find_all("td")

        title = products_tds[0].find("a").text
        calories = products_tds[1].text
        proteins = products_tds[2].text
        fats = products_tds[3].text
        carbohydrates = products_tds[4].text

        product_info.append({
            "title": title,
            "calories": calories,
            "proteins": proteins,
            "fats": fats,
           "carbohydrates": carbohydrates
        })

        with open(f"data/{count}_{category_name}.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )
        with open(f"data/{count}_{category_name}.json", "a", encoding="utf-8") as file:
            json.dump(product_info, file, indent=4, ensure_ascii=False)

    count += 1
# Оповещение о количестве операций
    print(f"# Итерация {count}.{category_name} записан...")
    iteration_count = iteration_count - 1

    if iteration_count == 0:
        print("Работа завершена")
        break
    print(f"Осталось итераций-{iteration_count}")



