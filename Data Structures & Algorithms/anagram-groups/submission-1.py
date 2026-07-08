class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter

        # sorting approach
        visited = set()
        sublists = []
        n = len(strs)  

        for i in range(n):  
            if i in visited:
                continue
            anagrams_sublist = [strs[i]] 
            visited.add(i)  
            for j in range(i + 1, n):   
                if j in visited:
                    continue
                if self.isAnagram(strs[i], strs[j]): # sorted(strs[i]) == sorted(strs[j])
                    anagrams_sublist.append(strs[j])
                    visited.add(j)
            sublists.append(anagrams_sublist)
        
        return sublists

    def isAnagram(self, str1, str2):
        str1_count = Counter(str1)
        str2_count = Counter(str2)

        if len(str1_count) != len(str2_count):
            return False

        for s_letter in str1_count:
            if str1_count[s_letter] != str2_count.get(s_letter, 0):
                return False
        
        return True