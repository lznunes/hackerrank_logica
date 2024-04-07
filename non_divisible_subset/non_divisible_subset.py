#SOLVED
#https://www.hackerrank.com/challenges/non-divisible-subset/problem


s1 = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
#s = [19,10,12,10,24,25,22]
s2 = [1,7,2,4]
k1 = 7
k2 = 3



def non_divisible_subset(s, k):
    # Cria uma lista com k elementos, inicializados com 0.
    #  Essa lista é usada para contar quantos números em S têm cada resto quando divididos por k.
    remainder_count = [0] * k


    #Percorre cada elemento e incrementa o contador correspondente
    for num in s:
        remainder_count[num % k] += 1

    #nicializa a variável mmax_subset_size com o valor mínimo
    mmax_subset_size = min(remainder_count[0], 1)


    for i in range(1, (k + 1) // 2):
        max_loop = max(remainder_count[i], remainder_count[k - i])
        mmax_subset_size += max_loop
    
    if (k % 2 == 0):
        mmax_subset_size += min(remainder_count[k // 2], 1)

    return mmax_subset_size

    




print(non_divisible_subset(s1, k1))
