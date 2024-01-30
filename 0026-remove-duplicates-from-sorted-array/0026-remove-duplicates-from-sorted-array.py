class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        a = 0
        for i in range(1,l):
            if nums[i-1] != nums[i]:
                a += 1
                nums[a] = nums[i]
        del nums[a+1:]