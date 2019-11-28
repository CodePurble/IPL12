inStr = input()

inStr = inStr.split(' ')

C = int(inStr[0])
N = int(inStr[1])

cost = []
sell = []

i = N;

while(i > 0):
    prices = input()
    prices = prices.split(' ')
    cost.append(prices[0])
    sell.append(prices[1])
    i -= 1

