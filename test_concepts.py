k = 7
s = [8, 9, 10, 11, 12, 13, 14]


def divible_remider(k, s):
    remider = [0] * k
    for n in s:
        remider[n % k] += 1
    max_remider = min(remider[0],1)
    for y in range(1, k-1):
        max_remider += max(remider[y], remider[k])
    
    print(remider, max_remider)


divible_remider(k, s)