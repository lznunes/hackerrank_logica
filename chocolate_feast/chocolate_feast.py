"""import modules."""
import os

def chocolate_feast(number_n, number_c, number_m):
    """Function chocolate_feast"""

    total = number_n // number_c
    wraper = total
    while wraper >= number_n:
        wraper += 1 - number_n
        wraper += 1
    return total

if __name__ == '__main__':
    #
    current_directory = os.getcwd()
    file_path_output = os.path.join(current_directory, 'chocolate_feast/out_chocolate_feast.txt')
    file_path_input = os.path.join(current_directory, 'chocolate_feast/in_chocolate_feast.txt')
    #
    with open(file_path_input, 'r', encoding="utf-8") as fptr: # lendo arquivo de entrada
        t = int(fptr.readline())
    #
        for t_itr in range(t):

            first_multiple_input = fptr.readline().split()

            n = int(first_multiple_input[0])

            c = int(first_multiple_input[1])

            m = int(first_multiple_input[2])

            result = chocolate_feast(n, c, m)

            print(result)


    fptr.close()

