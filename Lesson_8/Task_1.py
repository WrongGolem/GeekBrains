import re


def email_parse(email_addrees):
    pattern = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+\.\w+)$')
    result = pattern.match(email_addrees)
    if not result:
        raise ValueError(f'Электронный адресс неверный: {email_addrees}')
    return result.groupdict()


print(email_parse('someone@geekbrains.ru'))
# {'username': 'someone', 'domain': 'geekbrains.ru'}

