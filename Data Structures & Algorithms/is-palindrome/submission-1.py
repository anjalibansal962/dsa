class Solution:
    def isPalindrome(self, s: str) -> bool:
        # preprocessing -> uses etra space
        s = re.sub(r"[^a-zA-Z0-9]", "", s)      # re.sub(match_case, replace_case, str)

        # reverse approach
        '''rev = ''.join(reversed(s))      # reversed() returns a reverse iterator not the reversed str
        if s == rev:
            return True
        return False'''

        # 2 pointer approach
        l = 0
        r = len(s) - 1
        while l < r:    # l == r compares letter with itself, not required for palindrome
            if not s[l].isalnum():     # skip char if not alphanumeric instead of preprocessing str
                l += 1
            if not s[r].isalnum():      # str is immutable, so any modifications if persistant are new space
                r -= 1
            if s[l].lower() != s[r].lower():    # in place lowercase comparison of chars to avoid preprocessing space
                return False
            l += 1
            r -= 1
        return True
