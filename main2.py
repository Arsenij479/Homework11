def main2():
    import random
    #Словарь известных людей
    FAMOUS_PEOPLE = {'Григорий Лепс': 'Певец', 'Михаил Круг': 'Певец',
                    'Дима Билан': 'Певец', 'Shaman': 'Певец',
                    'Сергей Бурунов': 'Актёр', 'Джеки Чан': 'Актёр',
                    'Том Холланд': 'Актёр', 'Роберт Дауни-младший': 'Актёр',
                    'Эльдар Рязанов': 'Режиссёр', 'Альфред Хичкок': 'Режиссёр'}

    rounds = int(input('Сколько раз вы хотите играть?:'))
    for i in range(rounds):
            #Выбираем случайного человека
            name, date = random.choice(list(FAMOUS_PEOPLE.items()))
            #Спрашиваем кто он такой
            ansaer = input(f'Кто он такой {name}')
            #Проверка условия
            if ansaer == date:
                print('Верно')
            else:
                print('Неверно')
            print('Пока')

print('Добро пожаловать в игру Известный человек')
name = input('Как тебя зовут?')

print('Отлично!', name)
answer = input('И так ты готов?:')

if answer == 'Да':
    main2()
elif answer == 'Нет':
    print(('Готовься тогда!'))
else:
    print('Что ты хочешь от меня?')
