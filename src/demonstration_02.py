"""
Demonstration #2

Given a non-empty array of integers `nums`, every element appears twice except except for one. Write a function that finds the element that only appears once.

Examples:

- single_number([3,3,2]) -> 1
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""
def single_number(nums):
    # Your code here
    #holy crap this is super fragile
    # every number needs to specifically appear twice, and not more, except one.
    nums.sort()
    for i in range(0, len(nums), 2):
        if i + 1 < len(nums) and nums[i] != nums[i + 1]:
            return nums[i]
    if nums[-1] != nums[-2]:
        return nums[-1]

def single_number(nums):
    set
