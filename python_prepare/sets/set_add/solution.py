# Read the number of inputs
N = int(input())

# Collect unique inputs in a set directly with a comprehension
s = {input() for _ in range(N)}

# Print the size of the set, which represents the count of unique items
print(len(s))
