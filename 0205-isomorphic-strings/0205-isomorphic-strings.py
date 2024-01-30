class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        st = {}
        ts = {}
        for i,j in zip(s,t):
            if i in st and st[i]!=j:
                return False
            elif j in ts and ts[j]!=i:
                return False
            else:
                st[i]=j
                ts[j]=i
        return True   