class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        vowels_of_s = []
        for i in s:
            if i in vowels:
                vowels_of_s.append(i)
        vowels_of_s.reverse()
        output = []
        j=0
        for i in range(len(s)):
            if s[i] in vowels:
                output.append(vowels_of_s[j])
                j+=1
            else:
                output.append(s[i])
        return (''.join(output))