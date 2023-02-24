# Leetcode problem

# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are
# (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

in_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]

def max_water_container(height: list[int]) -> int:
    max_water = 0

    for i in range(len(in_list)):
        for j in range(len(in_list)):
            water = min(height[i], height[j]) * abs(i - j)
            if water > max_water:
                max_water = water
    return max_water


print(max_water_container(in_list))
