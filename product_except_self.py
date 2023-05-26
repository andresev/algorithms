def productExceptSelf(nums: list[int]):
    ans = [0] * (len(nums))
    prefix = 1

    for i in range(len(nums)):
        ans[i] = prefix
        prefix *= nums[i]

    postfix = 1

    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= postfix
        postfix *= nums[i]

    print(ans)
