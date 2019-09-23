def pal(str):
    return(str == reversed(str))

N = int(input())

words = []
for i in range(1, N+1):
    words.append(input())


print(N, words)
res = []

for i in range(T):
    for j in range(len(words[i])):
        if(words[i][])