import re

from bs4 import BeautifulSoup

with open('../site/index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
#поиск конкретного тэга и вывод его содержимого
#title = soup.title
#print(title)
#print(title.text)
#print(title.string)
# функции .find()-поиск до первого совпадения (можно вывести текстом)
# .find_all() поиск всех элементов и передача их списком (нельзя вывести текстом)
#page_h1 = soup.find('h1')
#print(page_h1.text)
#page_all_h1 = soup.find_all('h1')
#print(page_all_h1)
# Для печати всех вариантов из полного поиска можно воспользоваться циклом
#for item in page_all_h1:
    #print(item.text)
#user_name = soup.find("div", class_="user__name")
#print(user_name.text.strip())
# обрезает лишние пробелы .strip()
#user_name = soup.find("div", class_="user__name").find("span").text
#print(user_name)
#user_name = soup.find("div", {"class": "user__name"}).find("span").text
#print(user_name)
#find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
#print(find_all_spans_in_user_info)
#for item in find_all_spans_in_user_info:
   # print(item.text)
# Результат поиска find_all это список поэтому можно применять функции списка
#print(find_all_spans_in_user_info[1])
#print(find_all_spans_in_user_info[1].text)

#Находим ссылки на сранице
#social_links = soup.find(class_="social__networks").find('ul').find_all('li')
#print(social_links)
#for item in social_links:
    #print(item.text)

# вытаскиваем ссылки из атрибута "href" тега "а"
#all_a = soup.find_all("a")

#for item in all_a:
#    item_text = item.text
#    item_url = item.get("href")
#    print(f"{item_text}-{item_url}")

# Элементы перемещения по DOM-дереву .find_parent() и .find_parents()
#post_div = soup.find(class_="post__text").find_parent()
#print(post_div)

#post_div = soup.find(class_="post__text").find_parent('div', 'user__post')
#print(post_div)

#post_div = soup.find(class_="post__text").find_parents('div', 'user__blog__wall')
#print(post_div)

# Элементы перемещения по DOM-дереву .next_element() или .find_next() и .previous_element()
#(Принимает переносы строки, для избежания применять повторно

#next_el = soup.find(class_="post__title").next_element.next_element.text
#print(next_el)

#next_el = soup.find(class_="post__title").find_next().text
#print(next_el)

#next_el = soup.find(class_="post__title").previous_element.previous_element
#print(next_el)

#next_el = soup.find(class_="post__title").previous_element.text
#print(next_el)

# Элементы возвращают следующий и предыдущий элемент тега
# .find_next_sibling()  .find_previous_sibling()

#next_sib = soup.find(class_="post__title").find_next_sibling()
#print(next_sib.text)

#next_sib = soup.find(class_="post__title").find_next_siblings()
#print(next_sib)

#for item in next_sib:
#    print(item.text)

#prev_sib = soup.find(class_="post_date").find_previous_sibling()
#(prev_sib.text)
#prev_sib = soup.find(class_="post__text").find_previous_siblings()
#print(prev_sib)

#for item in prev_sib:
 #   print(item.text)
#post_title = soup.find(class_="post_date").find_previous_sibling().find_next().find_next().text

#print(post_title)

#вытаскиваем значения атрибутов из тэгов

#links = soup.find(class_='some__links').find_all('a')
#print(links)

#for link in links:
#    link_href_attr = link.get('href')
#    link_href_attr1 = link['href']

#    link_data_attr = link.get('data-attr')
#    link_data_attr = link['data-attr']

#    print(link_href_attr)
#    print(link_data_attr)

#Найдем тэг по части слова в нём

find_a_by_text = soup.find('a', text=re.compile("Одежда"))
print(find_a_by_text)

find_all_col = soup.find_all(text=re.compile("([Оо])дежда"))
print(find_all_col)