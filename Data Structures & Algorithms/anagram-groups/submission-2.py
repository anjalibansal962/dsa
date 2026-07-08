class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # my approach: O(n^2 . k)
        '''from collections import Counter

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
        
        return True'''

        # optimal approach
        from collections import defaultdict

        anagrams_sublists = defaultdict(list)   # automatically initializes a new key to [] (specified as list in the argument) in the dictionary

        for s in strs:
            key = ''.join(sorted(s))    
            # joins letters of a string without space into a word in a sorted order. 
            # e.g. if s = eat, key = aet
            anagrams_sublists[key].append(s)

        return list(anagrams_sublists.values())



