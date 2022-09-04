
from collections import Counter


'''def countMaxOperations(s, t):
    count = 0
    while(len(s) > 0):
        for i in t:
            if i not in s:
                return max(0, count)
            else:
                s.remove(i)
        count += 1

    return count

    pass'''


class Solution:
    def rearrangeCharacters(self, s: str, t: str) -> int:
        mi = 999999999
        s = Counter(s)
        t = Counter(t)
        for i in t.elements():
            mi = min(mi, s[i] // t[i])
        return mi


s = list(input())
t = list(input())

obj = Solution()
# print(countMaxOperations(s, t))
print(obj.rearrangeCharacters(s, t))
