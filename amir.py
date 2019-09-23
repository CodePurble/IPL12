inStr = input()

inStr = inStr.split(' ')

n = int(inStr[0])
m = int(inStr[1])

days = 0
count = 1

morn = n
eat = n 
# eve = eat

if(m < 2):
    print()
elif(n == 0):
    print(0)
else:
    while(eat > 0):
        eat -= 1
        morn = eat
        if(count % m == 0):
            eat += 1
        count += 1
        days += 1

    print(days)