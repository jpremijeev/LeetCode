class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        answer = {}
        for i in arr:
            if i in answer:
                answer[i] += 1
            else:
                answer[i] = 1
        return len(answer.values()) == len(set(answer.values()))        