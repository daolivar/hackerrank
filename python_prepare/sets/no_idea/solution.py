# Read integers n (number of elements in array) and m (number of elements in sets A and B)
# We assign them to _ because they are not used in the code
_, _ = map(int, input().split())  # Intentionally unused variables

# Read the list of elements, converting each to an integer
arr = list(map(int, input().split()))

# Read set A from input, converting each element to an integer and storing it in a set
A = set(map(int, input().split()))

# Read set B from input, converting each element to an integer and storing it in a set
B = set(map(int, input().split()))

# Initialize happiness score to 0
happiness = 0

# Iterate over each element in arr
for i in arr:
    # Increment happiness if the element is in set A
    if i in A:
        happiness += 1
    # Decrement happiness if the element is in set B
    if i in B:
        happiness -= 1

# Print the final happiness score
print(happiness)
