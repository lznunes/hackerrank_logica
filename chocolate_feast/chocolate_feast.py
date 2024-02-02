#https://www.hackerrank.com/challenges/chocolate-feast/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
import os

def chocolate_feast(total_money, chocolate_cost, wrappers_needed):
    """
    Calculates the total number of chocolates Brenno can eat.

    Parameters:
    - total_money: Amount of money Brenno has.
    - chocolate_cost: Cost of each chocolate.
    - wrappers_needed: Number of wrappers needed to exchange for a free chocolate.

    Returns:
    - Total number of chocolates Brenno can eat.
    """
    chocolates_bought = total_money // chocolate_cost
    wrappers = chocolates_bought

    while wrappers >= wrappers_needed:
        # Exchange wrappers for a free chocolate
        wrappers += 1 - wrappers_needed
        chocolates_bought += 1

    return chocolates_bought

if __name__ == '__main__':
    # Set file paths for input and output
    current_directory = os.getcwd()
    file_path_output = os.path.join(current_directory, 'chocolate_feast/out_chocolate_feast.txt')
    file_path_input = os.path.join(current_directory, 'chocolate_feast/in_chocolate_feast.txt')

    # Read input file
    with open(file_path_input, 'r', encoding="utf-8") as fptr:
        # Read the number of test cases
        num_test_cases = int(fptr.readline())

        # Process each test case
        for _ in range(num_test_cases):
            # Read parameters for each test case
            params = list(map(int, fptr.readline().split()))
            total_money, chocolate_cost, wrappers_needed = params

            # Calculate and print the result for the current test case
            result = chocolate_feast(total_money, chocolate_cost, wrappers_needed)
            print(result)

    # Close the file
    fptr.close()
