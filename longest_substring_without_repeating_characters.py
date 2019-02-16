class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def n_begin(s,n):
            exists = {}
            sub = []
            s = s[n:]
            # print("Testing",s)
            for char in s:
                if char not in exists:
                    exists[char] = 1
                    sub.append(char)
                else:
                    # print("Result:",len(sub))
                    return len(sub)
            return len(sub)
        maxim = 0
        for ind in range(0,len(s)):
            longest = n_begin(s,ind)
            if longest > maxim:
                maxim = longest
        return maxim

