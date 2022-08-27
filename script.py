import array as arr
import random

prices = arr.array('i', [])
for i in range(0, 20):
    prices.append(random.randint(2000, 3000))
# print('price', prices[i])

max_price = 2500
sum_price = 0
for i in range(0, len(prices)):
    if prices[i] > max_price:
        sum_price += prices[i]

print('sum prices more than max price', sum_price)


