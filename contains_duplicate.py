def containsDuplicate(nums: list[int]) -> bool:
    valueRepeat = {}
    for i, num in enumerate(nums):
        if num in valueRepeat:
            print(valueRepeat[3])
            print(True)
            return True
        else:
            valueRepeat[num] = i
    print(False)
    return False
