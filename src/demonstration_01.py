"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""
def two_sum(nums, target):
    setOfNums = set(nums)
    for i in range(len(nums)):
        if target - nums[i] in setOfNums:
            return [i, nums.index(target - nums[i])]

def two_sumAttemptTwo(nums, target):
    dictionary = {}
    for i, n in enumerate(nums):
        print(f"i is {i} and n is {n}")
        dictionary[n] = i
    for i in range(len(nums)):
        if nums[i] - target in dictionary:
            return [ i, dictionary[nums[i] - target] ]

if __name__ == "__main__":
    print(two_sumInstructor([2,5,9,13], 7))
    assert two_sumInstructor([2,5,9,13], 7) == [0,1], "should be [0,1]"

def two_suminstrtuctor(nums, target):
    dict = {}

    for i in range(len(nums)):
        dict[nums[i]] = i

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in dict and dict[complement] != i
            return [i, dict[target - nums[i]]
    return "no solution found"
