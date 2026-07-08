class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force
        # create a counter dict for each nums
        # sort the dict by values
        # return keys only using dict[: k] split
        
        from collections import Counter

        nums_count = Counter(nums)
        # print(nums_count)
        # print(sorted(nums_count))
        top_freq = (sorted(nums_count.items(), key = lambda item: item[1], reverse = True))

        out = []

        for i in range(k):
            out.append(top_freq[i][0])
        return out
            
    