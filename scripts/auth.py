"""
Регистрация, авторизация, восстановление пароля пользователя, основываясь на данных,
хранящихся в базе данных
"""


import sqlite3


db = sqlite3.connect('../db/registration.db')

cur = db.cursor()

cur.execute('''create table if not exists users_data(
            UserID integer primary key autoincrement,
            Login text not null,
            Password text not null,
            Code integer not null);''')
db.commit()

user_data = ('Ivan', 'qwer1234', 1234)

cur.execute('''insert into users_data ('Login', 'Password', 'Code')
            values (?, ?, ?);''', user_data)
db.commit()

action = ''
while action not in ('1', '2', '3'):
    action = input('Выберите действие: регистрация(1), авторизация(2),'
                   'восстановление пароля(3) ')
    if action not in ('1', '2', '3'):
        print('Некорректный ввод. Попробуйте еще раз.')

if action == '1':
    cur.execute('''select * from users_data;''')
    exists_logins = cur.fetchall()
    list_logins = []
    for login in exists_logins:
        list_logins.append(login[1])

    new_login = ''
    while new_login == '' or new_login in list_logins:
        new_login = input('Введите новый логин: ')
        if new_login == '':
            print('Логин не может быть пустым. Попробуйте еще раз.')
        elif new_login in list_logins:
            print('Пользователь с таким логином уже существует, выберите другой.')

    new_password = ''
    while new_password == '':
        new_password = input('Введите ваш новый пароль: ')
        if new_password == '':
            print('Пароль не должен быть пустым. Введите другой.')

    while True:
        new_code = input('Введите код, состоящий из четырёх цифр: ')
        if len(new_code) != 4:
            print('Код должен состоять из четырех цифр. Попробуйте еще раз.')
            continue
        try:
            new_code = int(new_code)
            break
        except ValueError:
            print('Код должен состоять из четырех цифр. Попробуйте еще раз.')

    new_user_data = (new_login, new_password, new_code)

    cur.execute('''insert into users_data ('Login', 'Password', 'Code')
                values (?, ?, ?);''', new_user_data)
    db.commit()
    print('Регистрация прошла успешно.')

elif action == '2':
    cur.execute('''select * from users_data;''')
    exists_users = cur.fetchall()

    auth_login = ''
    while auth_login == '':
        auth_login = input('Введите свой логин: ')
        if auth_login == '':
            print('Логин не должен быть пустым. Попробуйте еще раз.')

    auth_password = ''
    while auth_password == '':
        auth_password = input('Введите свой пароль: ')
        if auth_password == '':
            print('Пароль не должен быть пустым. Попробуйте еще раз.')

    count = 0
    for users in exists_users:
        if users[1] == auth_login and users[2] == auth_password:
            print('Авторизация в системе прошла успешно.')
            count += 1
            break
    if count == 0:
        print('Пользователя с таким логином и/или паролем не существует.')

elif action == '3':
    cur.execute('''select * from users_data;''')
    exists_users = cur.fetchall()

    recover_login = ''
    while recover_login == '':
        recover_login = input('Введите свой логин: ')
        if recover_login == '':
            print('Логин не должен быть пустым. Попробуйте еще раз.')

    while True:
        recover_code = input('Введите код, состоящий из четырёх цифр: ')
        if len(recover_code) != 4:
            print('Код должен состоять из четырех цифр. Попробуйте еще раз.')
            continue
        try:
            new_code = int(recover_code)
            break
        except ValueError:
            print('Код должен состоять из четырех цифр. Попробуйте еще раз.')

    count = 0
    recover_id = 0
    for users in exists_users:
        if users[1] == recover_login and users[3] == int(recover_code):
            count += 1
            recover_id = users[0]
            break

    if count == 0:
        print('Пользователя с таким логином и/или кодом не существует.')

    else:
        recover_password = ''
        while recover_password == '':
            recover_password = input('Введите новый пароль: ')
            if recover_password == '':
                print('Пароль не должен быть пустым. Попробуйте еще раз.')

        recover_data = (recover_password, recover_id)
        cur.execute('''update users_data set Password = ? where UserID = ?;''', recover_data)
        db.commit()
        print('Пароль был успешно изменен.')
