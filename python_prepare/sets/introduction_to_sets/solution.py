def average(array):
    # Convert the input list 'array' into a set to remove duplicates
    integer_set = set(array)

    # Calculate the sum of all unique elements in the set
    sum_heights = sum(integer_set)

    # Return the average by dividing the sum by the number of unique elements
    return float(sum_heights / len(integer_set))

if __name__ == '__main__':
    # Read an integer 'n' representing the number of elements in the array (not used directly in the function)
    n = int(input())

    # Read the input array, map the elements to integers, and convert it to a list
    arr = list(map(int, input().split()))

    # Call the average function and store the result
    result = average(arr)

    # Print the result (average of unique elements)
    print(result)
