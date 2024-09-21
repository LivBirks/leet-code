def removeDuplicates(nums: list[int]) -> int:
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
    print(nums)
    return l

print(removeDuplicates([1,1,2]))
