# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

from random import choice


def get_jokes(n, no_doubles=True):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    res = []
    if no_doubles:
        res2 = []
    for _ in range( n ):
        tmp = []
        if n > 5:
            no_doubles = False
        if no_doubles:
            new = choice( nouns )
            while new in res2:
                new = choice( nouns )
            tmp.append( new )

            new = choice( adverbs )
            while new in res2:
                new = choice( adverbs )
            tmp.append( new )

            new = choice( adjectives )
            while new in res2:
                new = choice( adjectives )
            tmp.append( new )
        else:
            tmp.append( choice( nouns ) )
            tmp.append( choice( adverbs ) )
            tmp.append( choice( adjectives ) )
        res.append( ' '.join( tmp ) )
        if no_doubles:
            res2.extend( tmp )
    return res


print( get_jokes( n=5 ) )
