def twoSum(nums, target):
    complements = {}
    for index, num in enumerate(nums):
        if num in complements:
            print([complements[num], index])
        else:
            complements[target - num] = index
