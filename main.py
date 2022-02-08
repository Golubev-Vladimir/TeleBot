import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4 and pip install lxml
import json  # pip install simplejson
import telebot  # pip install pytelegrambotapi
from termcolor import colored, cprint  # https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.4.730 Yowser/2.5 Safari/537.36'}

urls = ['https://www.citilink.ru/product/umnaya-kolonka-yandex-stanciya-lait-fioletovyi-yndx-00025-1547233/',
        'https://novosibirsk.e2e4online.ru/catalog2/Umnye_gadzhety_i_suveniry/Prochie_umnye_gadzhety/Umnaya_kolonka_YAndeks_Stantsiya_Lajt_5W_Alisa_Bluetooth_ultrafiolet_YNDX-00025_Purple.html',
        'https://www.eldorado.ru/cat/detail/umnaya-kolonka-s-alisoy-yandeks-stantsiya-layt-ultraviolet-yndx-00025p/',
        'https://kotofoto.ru/shop/uid_484395_umnaya_kolonka_yandeks_stantsiya_layt_yndx_00025_purple_fioletovaya.html',
        'https://www.dns-shop.ru/product/4ce98c9fbf612ff1/umnaa-kolonka-andeks-stancia-lajt-fioletovyj/',
        'https://www.mvideo.ru/products/umnaya-kolonka-novaya-yandeks-stanciya-mini-s-chasami-chernyi-oniks-10029476',
        'https://www.wildberries.ru/catalog/38327160/detail.aspx?targetUrl=XS',
        'https://sbermegamarket.ru/catalog/details/portativnaya-kolonka-yandeks-stanciya-layt-ultraviolet-yndx-00025p-100028813043/#?related_search=портативная+колонка+яндекс.+станция+лайт+ultraviolet+%28yndx-00025p%29',
        'https://www.technocity.ru/catalog/detail/795570/'
        ]
shortUrls = []  # формируем пустой список, чтобы добавить в него короткие имена сайтов из списка 'urls'
for url in urls:
    shortUrls.append(url.split('/')[2])

index = -1
for url in urls:  # проверяем ответы с сайтов
    index = index + 1
    try:
        response = requests.get(url, headers=headers)  # обращаемся к url напрямую c IDE с юзер-агентом
        print(f'индекс - {index}, ответ - {response.status_code}, {shortUrls[index]}')
    except:
        print(colored(f'индекс - {index}, ответ - нет, {shortUrls[index]}', 'yellow'))  # выдеяем те, что не найдены
print()

# 0
try:
    response0 = requests.get(urls[0])  # обращаемся к url напрямую по первой ссылке (url)
    soup0 = BeautifulSoup(response0.text, 'lxml')  # Парсим url, используя библиотеку BeautifulSoup
    tag0 = soup0.find_all('script',
                          type="application/ld+json")  # Находим нужный тег, в котором содержится искомый элемент (price в данном случае находится в json)
    if len(tag0) == 0:
        priceProduct0 = 'not found'
        print(f'{priceProduct0} {shortUrls[0]}')
        print()
    else:
        for t in range(0,
                       len(tag0)):  # с помощью цикла проходимся по всем найденным тегам, прокладывая пути к нужному значению
            try:
                path0 = tag0[t].contents[0]
                path_str0 = str(path0)
                path_dict0 = json.loads(path_str0)
                nameProduct0 = path_dict0['name']
                path_price0 = path_dict0['offers']
                priceProduct0 = path_price0['price']
                if priceProduct0 == '0':
                    priceProduct0 = 'нет в наличии'
                print(f'Описание товара - {nameProduct0}')
                print(f'Стоимость данного товара - {priceProduct0} руб. (по данным сайта: {shortUrls[0]})')
            except:
                print('не распознано')

except:  # если не может проложить маршрут
    priceProduct0 = 'нет связи с'
    print(f'{priceProduct0} {shortUrls[0]}')
print()

# 1
try:
    response1 = requests.get(urls[1])
    soup1 = BeautifulSoup(response1.text, 'lxml')
    tag1 = soup1.find_all('script', type="application/ld+json")
    if len(tag1) == 0:
        priceProduct1 = 'not found'
        print(f'{priceProduct1} {shortUrls[1]}')
    else:
        for t in range(0, len(tag1)):
            try:
                path1 = tag1[t].contents[0]
                path_str1 = str(path1)
                path_dict1 = json.loads(path_str1)
                nameProduct1 = path_dict1['name']
                path_price1 = path_dict1['offers']
                priceProduct1 = path_price1['price']
                if priceProduct1 == '0':
                    priceProduct1 = 'нет в наличии'
                print(f'Описание товара - {nameProduct1}')
                print(f'Стоимость данного товара - {priceProduct1} руб. (по данным сайта: {shortUrls[1]})')
            except:
                print('не распознано')

except:
    priceProduct1 = 'нет связи с'
    print(f'{priceProduct1} {shortUrls[1]}')
print()

response2 = requests.get(urls[2], headers=headers)
soup2 = BeautifulSoup(response2.text, 'lxml')
tag2 = soup2.find_all('div', class_="priceContainer")
tagname2 = soup2.find_all('h1', itemprop="name")
print(tagname2)
print()
# print(tagname4)
# 4
# try:
#     response4 = requests.get(urls[4])
#     soup4 = BeautifulSoup(response4.text, 'lxml')
#     tag4 = soup4.find_all('meta', itemprop="price")
#     tagname4 = soup4.find_all('h1', itemprop="name")
#     if len(tag4) == 0:
#         priceProduct4 = 'not found'
#         print(f'{priceProduct4} {shortname4}')
#         print()
#     else:
#         for t in range(0, len(tag3)):
#             try:
#                 priceProduct3 = tag3[t].attrs['content']
#                 nameProduct3 = tagname3[t].text
#                 if priceProduct3 == '0':
#                     priceProduct3 = 'нет в наличии'
#                 print(f'Описание товара - {nameProduct3}')
#                 print(f'Стоимость данного товара - {priceProduct3} (по данным сайта: {shortname3})')
#             except:
#                 print('не распознано')
# except:
#     priceProduct3 = 'нет связи с'
#     print(f'{priceProduct3} {shortname3}')
# print()
#
try:
    response3 = requests.get(urls[3])
    soup3 = BeautifulSoup(response3.text, 'lxml')
    tag3 = soup3.find_all('meta', itemprop="price")
    tagname3 = soup3.find_all('h1', itemprop="name")
    if len(tag3) == 0:
        priceProduct3 = 'not found'
        print(f'{priceProduct3} {shortUrls[3]}')
        print()
    else:
        for t in range(0, len(tag3)):
            try:
                priceProduct3 = tag3[t].attrs['content']
                nameProduct3 = tagname3[t].text
                if priceProduct3 == '0':
                    priceProduct3 = 'нет в наличии'
                print(f'Описание товара - {nameProduct3}')
                print(f'Стоимость данного товара - {priceProduct3} (по данным сайта: {shortUrls[3]})')
            except:
                print('не распознано')
except:
    priceProduct3 = 'нет связи с'
    print(f'{priceProduct3} {shortUrls[3]}')
print()

# 6
try:
    response6 = requests.get(urls[6])
    soup6 = BeautifulSoup(response6.text, 'lxml')
    tag6 = soup6.find_all('meta', itemprop="price")
    tagname6 = soup6.find_all('meta', itemprop="name")
    if len(tag6) == 0:
        priceProduct6 = 'not found'
        print(f'{priceProduct6} {shortUrls[6]}')
        print()
    else:
        for t in range(0, len(tag6)):
            try:
                priceProduct6 = tag6[t].attrs['content']
                nameProduct6 = tagname6[t].attrs['content']
                if priceProduct6 == '0':
                    priceProduct6 = 'нет в наличии'
                print(f'Описание товара - {nameProduct6}')
                print(f'Стоимость данного товара - {priceProduct6} (по данным сайта: {shortUrls[6]})')
            except:
                print('не распознано')
except:
    priceProduct6 = 'нет связи с'
    print(f'{priceProduct6} {shortUrls[6]}')
print()

# 8
try:
    response8 = requests.get(urls[8])
    soup8 = BeautifulSoup(response8.text, 'lxml')
    tag8 = soup8.find_all('script', type="text/javascript")
    tag80 = tag8[30].text
    tag800 = tag80.split('"products": [')[1].split(']')[0]

    tag8_dict = dict(tag800)
    print(type(tag8_dict))
    if len(tag8) == 0:
        priceProduct0 = 'not found'
        print(f'{priceProduct8} {shortUrls[8]}')
        print()
    else:
        for t in range(0, len(tag0)):
            try:
                path0 = tag0[t].text
                path_str0 = str(path0)
                path_dict0 = json.loads(path_str0)
                nameProduct0 = path_dict0['name']
                path_price0 = path_dict0['offers']
                priceProduct0 = path_price0['price']
                if priceProduct0 == '0':
                    priceProduct0 = 'нет в наличии'
                print(f'Описание товара - {nameProduct0}')
                print(f'Стоимость данного товара - {priceProduct0} руб. (по данным сайта: {shortUrls[0]})')
            except:
                print('не распознано')

except:  # если не может проложить маршрут
    priceProduct0 = 'нет связи с'
    print(f'{priceProduct0} {shortUrls[0]}')
print()

# Telegram
bot = telebot.TeleBot(
    '5011527506:AAG0ooGDtW42YHJ-PKfAvS3FTEMjWb3MNc4')  # подключение токен-бота, ключ получаем в Телеграм - @BotFather


@bot.message_handler(content_types=[
    'text'])  # объявление метода для получения текстовых сообщений (также можно ['text', 'document', 'audio']
def get_text_messages(message):
    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.from_user.id, f'{nameProduct0}\n\nСтоимость данного товара на cайтах, руб.:\n'
                                               f'{priceProduct0} - {shortUrls[0]}\n'
                                               f'{priceProduct1} - {shortUrls[1]}\n'
                                               f'{priceProduct3} - {shortUrls[3]}\n'
                                               f'{priceProduct6} - {shortUrls[6]}\n')
    else:
        bot.send_message(message.from_user.id, "Напиши <Привет>")


bot.polling(none_stop=True,
            interval=0)  # Теперь наш бот будет постоянно спрашивать у сервера Телеграмма «Мне кто-нибудь написал?»
