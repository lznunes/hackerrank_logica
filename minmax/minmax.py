import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    n_min = 0
    n_max = 0
    sums = []
    for i in range(0, len(arr)):
        n_arr = arr[:]
        n_arr.pop(i)
        sums.append(sum(n_arr))
    
    n_min = min(sums)
    n_max = max(sums)
    print(n_min, n_max)
    # Write your code here

def miniMaxSum_refator(arr):
    total_sum = sum(arr)
    min_sum = total_sum  # Inicializa o valor mínimo com a soma total
    max_sum = 0           # Inicializa o valor máximo com 0

    for num in arr:
        current_sum = total_sum - num  # Calcula a soma excluindo o número atual
        if current_sum < min_sum:
            min_sum = current_sum  # Atualiza o valor mínimo se necessário
        if current_sum > max_sum:
            max_sum = current_sum  # Atualiza o valor máximo se necessário

    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = [1,2,3,4,5]

    miniMaxSum(arr)
    miniMaxSum_refator(arr)