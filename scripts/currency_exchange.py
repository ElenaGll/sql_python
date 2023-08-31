import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By


db = sqlite3.connect('../db/exchanger.db')

cur = db.cursor()

cur.execute('''create table if not exists users_balance(
            UserID integer primary key autoincrement,
            Balance_RUB float not null,
            Balance_USD float not null,
            Balance_EUR integer not null
            );''')
db.commit()

cur.execute('''insert into users_balance (Balance_RUB, Balance_USD, Balance_EUR)
            values (100000, 1000, 1000)''')
db.commit()

options = webdriver.ChromeOptions()
options.add_argument('headless')
with webdriver.Chrome(options=options) as browser:
    url1 = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sca_esv=561614363&sxsrf=AB5stBhdIy-QOUCG5kWRvUiS3g84NPXNUQ%3A1693483470935&ei=zoHwZP_fOJXVwPAP-ryUoAw&ved=0ahUKEwj__t7F7YaBAxWVKhAIHXoeBcQQ4dUDCA8&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lp=Egxnd3Mtd2l6LXNlcnAiJdC60YPRgNGBINC00L7Qu9C70LDRgNCwINC6INGA0YPQsdC70Y4yDBAjGIoFGCcYRhiCAjILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEi3V1AAWI9VcAV4AZABAJgBZqAB4g6qAQQyNC4xuAEDyAEA-AEBqAIUwgIHECMYigUYJ8ICBBAjGCfCAgsQLhiABBixAxiDAcICCxAuGIAEGMcBGNEDwgIREC4YgAQYsQMYgwEYxwEY0QPCAg4QLhiABBixAxjHARjRA8ICCBAAGIAEGLEDwgINEC4YigUYxwEY0QMYQ8ICExAuGIoFGLEDGIMBGMcBGNEDGEPCAgcQABiKBRhDwgINEAAYigUYsQMYgwEYQ8ICDRAAGIoFGAoYARhDGCrCAgsQABiKBRgKGAEYQ8ICCRAAGIAEGAoYAcICBxAjGLECGCfCAg0QABiABBixAxiDARgKwgIHEAAYgAQYCsICBxAjGOoCGCfCAhAQABiKBRjqAhi0AhhD2AEBwgIQEAAYgAQYFBiHAhixAxiDAcICERAuGIoFGLEDGIMBGMcBGNEDwgIKEAAYgAQYFBiHAuIDBBgAIEGIBgG6BgYIARABGAE&sclient=gws-wiz-serp'
    browser.get(url1)
    rub_in_usd = browser.find_element(By.CSS_SELECTOR,
                                      'div.b1hJbf div.dDoNo.ikb4Bb.gsrt span.DFlfde.SwHCTb').text
    rub_in_usd = float(rub_in_usd.replace(',', '.'))

    url2 = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sca_esv=561614363&sxsrf=AB5stBihKQSMrIT5mhhDQ02uX9nQKSeseQ%3A1693483654467&ei=hoLwZK6XHKbawPAPlbeEcA&ved=0ahUKEwiu8qCd7oaBAxUmLRAIHZUbAQ4Q4dUDCA8&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lp=Egxnd3Mtd2l6LXNlcnAiH9C60YPRgNGBINC10LLRgNC-INC6INGA0YPQsdC70Y4yCxAAGIAEGLEDGIMBMgUQABiABDILEAAYgAQYsQMYgwEyBRAAGIAEMgsQABiABBixAxiDATIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESNcdUM8HWLEbcAR4AZABAJgBVqAB7gSqAQE5uAEDyAEA-AEBwgIKEAAYRxjWBBiwA8ICChAAGIoFGLADGEPCAgsQABiABBgKGAIYKsICDRAAGA0YgAQYsQMYgwHCAgcQABgNGIAEwgIPEAAYgAQYsQMYgwEYChgqwgIHEAAYgAQYCsICDRAAGIAEGLEDGIMBGArCAgYQABgHGB7CAggQABgHGB4YCuIDBBgAIEGIBgGQBgo&sclient=gws-wiz-serp'
    browser.get(url2)
    rub_in_eur = browser.find_element(By.CSS_SELECTOR,
                                      'div.b1hJbf div.dDoNo.ikb4Bb.gsrt span.DFlfde.SwHCTb').text
    rub_in_eur = float(rub_in_eur.replace(',', '.'))

    url3 = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D0%B5%D0%B2%D1%80%D0%BE&sca_esv=561614363&sxsrf=AB5stBgeEKzpc84T-dQXyfOjeBW3u3_giQ%3A1693483454546&ei=voHwZPaEIZ-GwPAPlP-UmAo&ved=0ahUKEwj22_a97YaBAxUfAxAIHZQ_BaMQ4dUDCA8&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D0%B5%D0%B2%D1%80%D0%BE&gs_lp=Egxnd3Mtd2l6LXNlcnAiI9C60YPRgNGBINC00L7Qu9C70LDRgNCwINC6INC10LLRgNC-MgcQIxiKBRgnMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESPkdUKAIWJoccAJ4AZABAJgBU6ABhgiqAQIxNbgBA8gBAPgBAcICChAAGEcY1gQYsAPCAgoQABiKBRiwAxhDwgILEAAYgAQYsQMYgwHCAg0QABiKBRixAxiDARhDwgIIEAAYgAQYsQPCAgoQABiABBgUGIcCwgIHEAAYigUYQ8ICBxAjGLECGCfCAg0QABiABBixAxiDARgKwgIHEAAYgAQYCsICChAAGIAEGLEDGAriAwQYACBBiAYBkAYK&sclient=gws-wiz-serp'
    browser.get(url3)
    eur_in_usd = browser.find_element(By.CSS_SELECTOR,
                                      'div.b1hJbf div.dDoNo.ikb4Bb.gsrt span.DFlfde.SwHCTb').text
    eur_in_usd = float(eur_in_usd.replace(',', '.'))

    url4 = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&sca_esv=561614363&sxsrf=AB5stBgWz1qDfCkats-wpoDUXTaiao9H8g%3A1693483773878&ei=_YLwZJ-lNZapwPAPnNC6uAw&ved=0ahUKEwjfl5nW7oaBAxWWFBAIHRyoDscQ4dUDCA8&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&gs_lp=Egxnd3Mtd2l6LXNlcnAiI9C60YPRgNGBINC10LLRgNC-INC6INC00L7Qu9C70LDRgNGDMgcQIxiKBRgnMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESMcoUKQLWOcmcAV4AZABAJgBeaABkgmqAQQxNS4xuAEDyAEA-AEBwgIKEAAYRxjWBBiwA8ICDRAAGEcY1gQYyQMYsAPCAgsQABiKBRiSAxiwA8ICChAAGIoFGLADGEPCAgsQABiABBixAxiDAcICEBAAGIAEGBQYhwIYsQMYgwHCAgkQABiABBgKGCrCAgoQABiABBgUGIcCwgIHEAAYgAQYCsICBhAAGBYYHsICCBAAGBYYHhgKwgIOEAAYgAQYChgqGEYYggLiAwQYACBBiAYBkAYK&sclient=gws-wiz-serp'
    browser.get(url4)
    usd_in_eur = browser.find_element(By.CSS_SELECTOR,
                                      'div.b1hJbf div.dDoNo.ikb4Bb.gsrt span.DFlfde.SwHCTb').text
    usd_in_eur = float(usd_in_eur.replace(',', '.'))


print('Добро пожаловать в наш обменный пункт, курс валют следующий:\n'
      f'1 USD = {rub_in_usd} RUB\n'
      f'1 EUR = {rub_in_eur} RUB\n'
      f'1 USD = {eur_in_usd} EUR\n'
      f'1 EUR = {usd_in_eur} USD\n')

while True:
    get_currency = input('Введите какую валюты желаете получить:\n'
                         '1 - RUB, 2 - USD, 3 - EUR\n')
    if get_currency not in ('1', '2', '3'):
        print('Неправильный ввод, попробуйте еще раз.')
    else:
        break

while True:
    sum_currency = input('Какая сумма Вас интересует?\n')
    try:
        sum_currency = int(sum_currency)
        if sum_currency < 1:
            print('Сумма должна быть больше нуля.')
        else:
            break
    except ValueError:
        print('Вы должны ввести сумму числом. Попробуйте еще раз.')

while True:
    give_currency = input('Какую валюту готовы предложить взамен?\n'
                          '1 - RUB, 2 - USD, 3 - EUR\n')
    if give_currency == get_currency:
        print('Выберите валюту отличную от предложенной.')
    elif give_currency not in ('1', '2', '3'):
        print('Неправильный ввод, попробуйте еще раз.')
    else:
        break

cur.execute('''select * from users_balance''')
all_data = cur.fetchone()
sum_rub = all_data[1]
sum_usd = all_data[2]
sum_eur = all_data[3]

if get_currency == '1':
    if give_currency == '2':
        necessary_usd = sum_currency / rub_in_usd
        if sum_usd >= necessary_usd:
            new_rub = sum_rub + sum_currency
            new_usd = sum_usd - necessary_usd
            update_data_rub = (new_rub, 1)
            update_data_usd = (new_usd, 1)
            cur.execute('''update users_balance set Balance_RUB = round(?, 2) where UserID = ?''',
                        update_data_rub)
            cur.execute('''update users_balance set Balance_USD = round(?, 2) where UserID = ?''',
                        update_data_usd)
            db.commit()
            print('Операция завершена успешно.')
        else:
            print('Недостаточная сумма на балансе для проведения операции.')
    else:
        necessary_eur = sum_currency / rub_in_eur
        if sum_eur >= necessary_eur:
            new_rub = sum_rub + sum_currency
            new_eur = sum_eur - necessary_eur
            update_data_rub = (new_rub, 1)
            update_data_eur = (new_eur, 1)
            cur.execute('''update users_balance set Balance_RUB = round(?, 2) where UserID = ?''',
                        update_data_rub)
            cur.execute('''update users_balance set Balance_EUR = round(?, 0) where UserID = ?''',
                        update_data_eur)
            db.commit()
            print('Операция завершена успешно.')
        else:
            print('Недостаточная сумма на балансе для проведения операции.')

elif get_currency == '2':
    if give_currency == '1':
        necessary_rub = sum_currency * rub_in_usd
        if sum_rub >= necessary_rub:
            new_usd = sum_usd + sum_currency
            new_rub = sum_rub - necessary_rub
            update_data_usd = (new_usd, 1)
            update_data_rub = (new_rub, 1)
            cur.execute('''update users_balance set Balance_USD = round(?, 2) where UserID = ?''',
                        update_data_usd)
            cur.execute('''update users_balance set Balance_RUB = round(?, 2) where UserID = ?''',
                        update_data_rub)
            db.commit()
            print('Операция завершена успешно.')
        else:
            print('Недостаточная сумма на балансе для проведения операции.')
    else:
        necessary_eur = sum_currency * eur_in_usd
        if sum_eur >= necessary_eur:
            new_usd = sum_usd + sum_currency
            new_eur = sum_eur - necessary_eur
            update_data_usd = (new_usd, 1)
            update_data_eur = (new_eur, 1)
            cur.execute('''update users_balance set Balance_USD = round(?, 2) where UserID = ?''',
                        update_data_usd)
            cur.execute('''update users_balance set Balance_EUR = round(?, 0) where UserID = ?''',
                        update_data_eur)
            db.commit()
            print('Операция завершена успешно.')
        else:
            print('Недостаточная сумма на балансе для проведения операции.')

elif get_currency == '3':
    if give_currency == '1':
        necessary_rub = sum_currency * rub_in_eur
        if sum_rub >= necessary_rub:
            new_eur = sum_usd + sum_currency
            new_rub = sum_rub - necessary_rub
            update_data_eur = (new_eur, 1)
            update_data_rub = (new_rub, 1)
            cur.execute('''update users_balance set Balance_EUR = round(?, 0) where UserID = ?''',
                        update_data_eur)
            cur.execute('''update users_balance set Balance_RUB = round(?, 2) where UserID = ?''',
                        update_data_rub)
            db.commit()
            print('Операция завершена успешно.')
        else:
            print('Недостаточная сумма на балансе для проведения операции.')
    else:
        necessary_usd = sum_currency * usd_in_eur
        if sum_usd >= necessary_usd:
            new_eur = sum_eur + sum_currency
            new_usd = sum_usd - necessary_usd
            update_data_eur = (new_eur, 1)
            update_data_usd = (new_usd, 1)
            cur.execute('''update users_balance set Balance_EUR = round(?, 0) where UserID = ?''',
                        update_data_eur)
            cur.execute('''update users_balance set Balance_USD = round(?, 2) where UserID = ?''',
                        update_data_usd)
            db.commit()
            print('Операция завершена успешно.')
        else:
            print('Недостаточная сумма на балансе для проведения операции.')
