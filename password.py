import random as r


pas = []
a = 0

bigLetters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z')

smallLetters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z')

nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

simbols = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '№', ';', ':', '?', '{', '}', ',',
           '.', '<', '>', '/', '[', ']', '~')


def save_data(q, y):
    try:
        with open('passlog.txt', 'a') as file:
            g = ''.join(y)
            file.write(str(f'login: {q} -- password: {g}\n'))
            print("Пароль и логин сохранены")
    except:
        print("Ошибка при сохранении результата в файл.")


def check_login():
    if (('.ru' in login[-3:] and len(login) >= 5) or ('.com' in login[-4:] and len(login) >= 6)) and '@' in login:
        try:
            with open('passlog.txt') as f:
                if login not in f.read():
                    print('Логин принят')
                    return True
                else:
                    print('Такой логин уже есть')
        except:
            return True

    else:
        print('Ваш логин не принят (в логине должно быть: ".ru" или ".com" и @:)')


def check_password():
    if password == 1:
        global pas
        pas = input('Пароль должен содержать: не менее 8 символов (1 заглавный буква; специальный символ) - ')
        l = list(pas)
        c = set(nums).intersection(l)
        v = set(smallLetters).intersection(l)
        b = set(bigLetters).intersection(l)
        f = set(simbols).intersection(l)
        if len(c) > 0 and len(v) > 0 and len(b) > 0 and len(f) > 0:
            return True
    elif password == 2:
        generate()
        return True
    else:
        print('не правильный запрос')


def generate():
    for i in range(5):
        first = str(nums[r.randint(0, len(nums) - 1)])
        second = smallLetters[r.randint(0, len(smallLetters) - 1)]
        third = bigLetters[r.randint(0, len(bigLetters) - 1)]

        pas.append(first)
        pas.append(second)
        pas.append(third)

    pas.reverse()
    pas.append(simbols[r.randint(0, len(simbols) - 1)])
    return True


while True:
    login = input('Введите логин: ')
    if check_login():
        break


while True:
    password = int(input('Выбери цыфру: 1 - создать свой пароль, 2 - сгенирировать надежный пароль: '))
    if check_password():
        print('Пароль принят')
        save_data(login, pas)
        break
