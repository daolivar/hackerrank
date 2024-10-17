if __name__ == '__main__':
    # Solution for PyPy3 on HackerRank

    # Read the first input which is an integer N, representing the number of elements
    N = int(input())

    # Read the next line containing N space-separated integers
    # Convert the input into a tuple of integers, then hash the tuple
    elements = hash(tuple(map(int, input().split())))

    # Print the hash value of the tuple
    print(elements)
