class Solution(object):
    def compress(self, chars):
        s = []
        curr = chars[0]
        count = 1
        for i in range(1,len(chars)):
            if chars[i] == curr:
                count += 1
            else:
                s.append(curr)
                if count > 1:                    
                    s.extend(str(count))
                count = 1
                curr = chars[i]

        s.append(curr)
        if count > 1:
            s.extend(str(count))
            
        chars[:len(s)] = s

        return len(s)