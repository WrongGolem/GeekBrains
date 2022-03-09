import requests

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
content = response.text

def currency_rates(currency):
    currency = currency.upper()
    if currency in content:
        for currency in content.split(f'{currency}')[1:]:
            currency_exit = currency.split('Value>')[1]
            print(currency_exit.split('<')[0], 'rubles on date:', response.headers['Date'])
    else:
        print('None')


#currency_rates('USD')
#currency_rates('eur')
#currency_rates('GBP')
#currency_rates('BER')
