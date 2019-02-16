class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 0
        max_palindrome = 0
        if len(s) == 0:
            return ""
        elif len(s) == 1:
            return s
        for n in range(0,len(s)):
            for m in range(n,len(s)):
                string = s[n:m+1]
                if string[::-1] == string:
                    # print(string, string[::-1])
                    if len(string) > max_length:
                        max_length = len(string)
                        max_palindrome = string
        return max_palindrome
                    
        
