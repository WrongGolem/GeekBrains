list_of_collegues = {}


def thesaurus(name):
    if name[0] not in list_of_collegues:
        list_of_collegues[name[0]] = name
    else:
        list_of_collegues[name[0]] = [list_of_collegues[name[0]], name]


thesaurus("Иван")
thesaurus("Мария")
thesaurus("Петр")
thesaurus("Илья")

print(list_of_collegues)
