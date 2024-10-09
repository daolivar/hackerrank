if __name__ == '__main__':
    # Read input values for x, y, z, and n
    x = int(input())  # Upper limit for variable i
    y = int(input())  # Upper limit for variable j
    z = int(input())  # Upper limit for variable k
    n = int(input())  # The sum that must not be matched

    # Create a list of all possible combinations of i, j, k where the sum i + j + k is not equal to n
    list = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
    
    # The resulting list contains lists of [i, j, k] where i is in range(x+1), j in range(y+1), k in range(z+1),
    # and the sum of i, j, k does not equal n.
    print(list)
