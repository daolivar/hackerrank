# Take input for the thickness of the 'H' shape
thickness = int(input())
c = 'H'  # Character used to build the shape

# Top Cone
for i in range(thickness):
    # Create the top cone using right and left justified 'H' characters
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    # Print two centered blocks of 'H', forming the vertical pillars
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    # Print a long horizontal belt across the middle, five times the thickness
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    # Print two centered blocks again, forming the bottom part of the vertical pillars
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    # Create the bottom cone by reversing the logic of the top cone and aligning it to the right
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
