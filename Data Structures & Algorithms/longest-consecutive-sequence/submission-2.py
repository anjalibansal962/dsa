class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force
        # sort set
        # max = 0
        # count = 0
        # for i: 1 -> n if num[i] - num[i-1] == 1
        # count += 1
        # else
        # if count > max
        # reset count
        # set count as new max
        # return max

        '''max_count = 0
        count = 1
        nums = self.custom_sort(list(set(nums)))
        n = len(nums)

        for i in range(1, n):
            if nums[i] - nums[i-1] == 1:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 1
        
        return max_count

    def custom_sort(self, nums: List[int]) -> List[int]:
        
        # needs to be O(n) t.c.
        q = deque()
        n = len(nums)
        l = 0
        r = n - 1
        
        while l <= r:
            if nums[l] > nums[r]:
                q.appendleft(nums[l])
                l += 1
            else:
                q.appendleft(nums[r])
                r -= 1
        return q'''

        # lookup approach
        nums = set(nums) 
        n = len(nums)  
        max_count = 0  
        if n != 0:
            count = 1
        else:
            return 0

        for num in nums:
            count = 1
            if num - 1 not in nums:     # checking if a num can even be the start of a consecutive sequence
                first_consecutive = num + 1
                while first_consecutive  in nums:
                    count += 1
                    first_consecutive  += 1
                if count > max_count:
                    max_count = count
        
        return max_count
