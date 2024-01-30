class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        if nums:
            for i in range(len(nums)):
                if nums[i] != val:
                    nums[a] = nums[i]
                    a += 1
        return a
        