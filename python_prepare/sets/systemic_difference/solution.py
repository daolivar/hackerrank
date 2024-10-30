# Read and ignore the first integer input
_ = input()
a = set(map(int, input().split()))  # Read the first set of integers

# Read and ignore the second integer input
_ = input()
b = set(map(int, input().split()))  # Read the second set of integers

# Calculate symmetric difference between sets a and b
symmetric_diff = a.symmetric_difference(b)

# Print each element in ascending order
for i in sorted(symmetric_diff):
    print(i)
