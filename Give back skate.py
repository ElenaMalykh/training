# Задача 3. Вирус
#
# Дима написал программу-вирус специально для того, чтобы проучить своего друга-должника,
# который никак не хочет возвращать скейтборд. Программа не даёт работать за компьютером и постоянно выводит на экран сообщение
# «Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!». Как только вводится правильный код, вирус удаляется.
# Напишите такую же программу, которую написал Дима.
#
#
#
# Пример:
#
# Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!
#
# Введите код: 1005
#
# Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!
#
# Введите код: 7777
#
# Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!
#
# Введите код: 0550
#
# Код верный, завершаю работу...

exit_code = "0550"  # int числа не могут начинаться с 0, поэтому надо использовать str
while True:
    print("Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!")
    user_code = input("Введите код: ")  # И тут соответственно не нужно приводить число к int типу
    if user_code == exit_code:
        print("Код верный, завершаю работу...")
        break


# my code:

while user_code := input('Enter password: ') != '0550':
  print('Computer has been blocked. First give back my skate, Than I will tell you the password')

print('Right')








