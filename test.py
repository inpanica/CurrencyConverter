from currency_converter import CurrencyConverter
from datetime import date
amount = 1000.1
oldcur = 'USD'
newcur = 'RUB'
c = CurrencyConverter()
print(c.convert(100, 'EUR', 'USD', date(2022, 3, 1)))
