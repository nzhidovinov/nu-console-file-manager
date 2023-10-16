import random

questions = {
    'Дата рождения Пушкина? ': ('06.06.1799', 'шестое июня 1799 года'),
    'Дата рождения Лермонтова? ': ('15.10.1814', 'пятнадцатое октября 1814 года'),
    'Дата рождения Есенина? ': ('03.10.1895', 'третье октября 1895 года'),
    'Дата рождения Гончарова? ': ('18.06.1812', 'восемнадцатое июня 1812 года'),
    'Дата рождения Толстова? ': ('09.09.1828', 'девятое сентября 1828 года'),

}


def victory(input_fn=input, output_fn=print):
    total = 5
    curr_answered = 0
    actual_questions = random.sample(sorted(questions), total)

    output_fn('Викторина начинается!')
    for q in actual_questions:
        ans = input_fn(q)
        if ans != questions[q][0]:
            output_fn(f'Правильный ответ: {questions[q][1]}')
        else:
            curr_answered += 1

    output_fn('Количество правильных ответов: ', curr_answered)
    output_fn('Количество ошибок: ', total - curr_answered)
    output_fn('Процент правильных ответов: ', 100 * curr_answered / total)
    output_fn('Процент неправильных ответов: ', 100*(1 - curr_answered / total))


if __name__ == '__main__':
    victory()
