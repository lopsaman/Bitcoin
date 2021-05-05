from bitcoin_value import currency

cur = currency("USD")
result = currency ("USD").fetch()
print("United states dollar")
print(result)
cur1= currency("EUR")
results = currency("EUR").fetch()
print("Euro")
print(results)