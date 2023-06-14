def missingNumber(nums):
    sorted_nums = sorted(nums)
    missing_num = [0]

    if 0 not in sorted_nums:
        print(0)
        return 0
    elif len(sorted_nums) not in sorted_nums:
        missing_num.pop()
        missing_num.append(len(sorted_nums))
        print(missing_num[0])
        return missing_num[0]

    for i, num in enumerate(sorted_nums):
        print(num, i)
        if num != i:
            missing_num.pop()
            missing_num.append(i)
            print(missing_num[0])
            return (missing_num[0])
    print(missing_num)
