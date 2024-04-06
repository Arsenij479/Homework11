import main2
print('Добро пожаловать в игру викторина')
name = input('Как тебя зовут?')

print('Отлично!', name)
answer = input('И так ты готов?:')

if answer == 'Да':
    main2()
elif answer == 'Нет':
    print(('Готовься тогда!'))
else:
    print('Что ты хочешь от меня?')