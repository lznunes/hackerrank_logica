#https://www.hackerrank.com/challenges/cut-the-sticks/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

import os

def cut_the_sticks(arr):
    """
    Cuts the sticks and returns a list of the remaining lengths after each cut.

    Parameters:
    - arr: List of stick lengths.

    Returns:
    - List containing the count of remaining sticks after each cut.
    """
    result = []

    while arr:
        # Record the count of sticks before each cut
        result.append(len(arr))
        
        # Find the minimum length of sticks
        min_stick = min(arr)
        
        # Cut the sticks by subtracting the minimum length
        arr = [x - min_stick for x in arr if x != min_stick]

    return result

if __name__ == '__main__':
    # Set the file path
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, 'cut_the_sticks/cut_the_sticks.txt')

    # Input: Read the list of stick lengths from user input
    arr = list(map(int, input().rstrip().split()))

    # Process the cuts
    result = cut_the_sticks(arr)

    # Output: Write the result to a file
    with open(file_path, 'w') as fptr:
        fptr.write('\n'.join(map(str, result)))
        fptr.write('\n')
