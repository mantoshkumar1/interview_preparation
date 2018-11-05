class Solution:
    def isPalinDrome(self, s):
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
            
        return True
    
    def get_str(self, arr, s):
        return "".join(arr) + s
    
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # todo: comp of program is O(n^2), improve it to make O(n)
        if self.isPalinDrome(s):
            return s
        
        s_len = len(s)
        prefix = []
        
        for i in range(s_len - 1, -1, -1):
            prefix.append(s[i])
            ans = self.get_str(prefix, s)
            if self.isPalinDrome(ans):
                return ans


a = Solution()
assert "abbaabba" == a.shortestPalindrome("aabba")
assert "aaacecaaa" == a.shortestPalindrome("aacecaaa")
assert "acbabca" == a.shortestPalindrome("abca")