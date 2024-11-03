class Solution:
    def removeDuplicates(self, nums: list) -> int:
        # l = k use l to store the last found duplicate
        # will start as one as zero is always the firt of its kind so not duplicate
        l = 1 
        # start with r = 1 and it will loop through the array from there
        for r in range(1, len(nums)):
            # check if r is not the same as the number before it, first time it will be comparing to l
            if nums[r] != nums[r -1]:
                # if they aren't duplicates make l the next number up in the sequence
                nums[l] = nums[r]
                # move l along to check the next number
                l += 1
        # return l as k
        return l
