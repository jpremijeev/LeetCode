class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i=0
        while i<len(flowerbed):
            if flowerbed[i] == 0 and (i==0 or flowerbed[i-1]==0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):        
                count+=1
                if count>=n:
                    return True        
                i+=2
            else:
                i+=1

        if count>=n:
            return True
        else:
            return False