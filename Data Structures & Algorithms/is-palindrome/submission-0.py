class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r"[^a-zA-Z0-9]", "", s)      # re.sub(match_case, replace_case, str)

        # reverse approach
        '''rev = ''.join(reversed(s))      # reversed() returns a reverse iterator not the reversed str
        if s == rev:
            return True
        return False'''

        # 2 pointer approach
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True