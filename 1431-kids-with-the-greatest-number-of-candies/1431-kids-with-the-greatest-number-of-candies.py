class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        max_candy = max(candies)
        for i in candies:
            if i+extraCandies >= max_candy:
                output.append(True)
            else:
                output.append(False)
        
        return output