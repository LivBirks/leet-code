def removeDuplicates(nums: list[int]) -> int:
    l = 1
    for r in range(1, len(nums)):
        if nums[r] == nums[r - 1]:
            nums[l] = nums[r +1]
        else:
            l += 1
    return l

removeDuplicates([1,1,2])
