class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force
        '''if len(s) != len(t)
            return False

        if sorted(s) != sorted(t):  # O(nlogn) + O(n)
            return False
        else:
            return True'''
        
        # using Counter 
        
        if len(s) != len(t):    # t.c. = O(1)
            return False
        
        from collections import Counter

        # Counter creates a dictionary of frequency of occurrence = {letter : letter_count}
        # t.c. = O(n)
        # s.c. = O(k) where k is number of distinct letters

        s_counts = Counter(s)
        t_counts = Counter(t)

        for s_letter in s_counts:
            if s_counts[s_letter] != t_counts.get(s_letter, 0):
                # dict.get(key, default_value) is used to search a value for a key without giving an error if the key doesn't exist
                return False

        return True