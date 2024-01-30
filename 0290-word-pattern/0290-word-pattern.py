class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_list = list(pattern)
        s_list = s.split()        
        
        if len(pattern) != len(s_list):
            return False
        
        sp = {}
        ps = {}

        for i,j in zip(p_list,s_list):
            if i in sp and sp[i] != j:
                return False
            elif j in ps and ps[j] != i:
                return False
            else:
                sp[i] = j
                ps[j]=i

        return True                  