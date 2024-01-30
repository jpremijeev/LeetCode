class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        l = len(nums)

        for i in nums:
            count_dict[i] = count_dict.get(i,0)+1

        sorted_items = sorted(count_dict.items(), key = lambda x: x[1], reverse = True)

        return (sorted_items[0][0])
