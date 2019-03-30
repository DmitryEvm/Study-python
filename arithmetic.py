true_answer = str((4 * 100) - 54)
user_answer = str(input('Решите пример:\n4 * 100 - 54 = '))
print('правильный ответ: ', true_answer)
print('ваш ответ: ', user_answer)
if user_answer == true_answer:
    print("Правильно!")
else:
    print("Не правильно!")
print()