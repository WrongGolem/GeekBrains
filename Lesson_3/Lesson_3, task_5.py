import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


# Вариант № 1 - простое решение задачи
def get_jokes(number):
    for unit in range(number):
        joke = f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}'
        print(joke)


get_jokes(4)

print('______________________________________________________________________________________________________')


# Вариант № 2 - уникальные аргументы
def get_jokes(number):
    for unit in range(number):
        random_noun = random.choice(nouns)
        random_adverbs = random.choice(adverbs)
        random_adjectives = random.choice(adjectives)
        nouns.remove(random_noun)
        adverbs.remove(random_adverbs)
        adjectives.remove(random_adjectives)
        print(random_noun, random_adverbs, random_adjectives)


get_jokes(5)
