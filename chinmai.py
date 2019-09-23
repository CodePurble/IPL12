# def ans(x):
#     res = 0
#     if(x%2 == 0):
#         for i in range(0, x+1, 2):
#             res += i**2
#     else:
#         for i in range(1, x+1, 2):
#             res += i**2

#     return res

def ans(x):
    if(x % 2 == 0):
        l = [i**2 for i in range(0, x+1, 2)]
    else:
        l = [i**2 for i in range(1, x+1, 2)]

    res = 0
    for i in l:
        res += i

    return res

T = int(input())

enns = []
for i in range(1, T+1):
    enns.append(int(input()))

sq = []

for i in range(T):
    sq.append(ans(enns[i]))

for x in sq:
    print(x)

    
