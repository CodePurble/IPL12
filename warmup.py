def warmup(str):
    total = 0

    s1 = str[:len(str)//2]
    s2 = str[(len(str)//2):]
    print(s1 + " " + s2)

    for char in s1:
        total += ord(char)

    for char in s2[1:]:
        total -= ord(char)

    if(total == 0):
        return True
    else:
        return False
    
print(warmup("abcdcba"))