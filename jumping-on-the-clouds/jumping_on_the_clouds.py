#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

c = [0,0,1,0,0,1,0]
count = 0


i = 0

while i < len(c):
    if i + 2 < len(c):
        if c[i+2] == 0 :
            count += 1
            i += 2
        elif c[i+1] == 0:
            count += 1
            i += 1
    elif i + 1 < len(c):
        if c[i+1] == 0 :
            count += 1
            i += 2



print(count)
