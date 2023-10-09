import random

questions = {
    'Дата рождения Пушкина? ': ('06.06.1799', 'шестое июня 1799 года'),
    'Дата рождения Лермонтова? ': ('15.10.1814', 'пятнадцатое октября 1814 года'),
    'Дата рождения Есенина? ': ('03.10.1895', 'третье октября 1895 года'),
    'Дата рождения Гончарова? ': ('18.06.1812', 'восемнадцатое июня 1812 года'),
    'Дата рождения Толстова? ': ('09.09.1828', 'девятое сентября 1828 года'),

}


def victory():
    total = 5
    curr_answered = 0
    actual_questions = random.sample(sorted(questions), total)

    print('Викторина начинается!')
    for q in actual_questions:
        ans = input(q)
        if ans != questions[q][0]:
            print(f'Правильный ответ: {questions[q][1]}')
        else:
            curr_answered += 1

    print('Количество правильных ответов: ', curr_answered)
    print('Количество ошибок: ', total - curr_answered)
    print('Процент правильных ответов: ', 100 * curr_answered / total)
    print('Процент неправильных ответов: ', 100*(1 - curr_answered / total))


if __name__ == '__main__':
    victory()