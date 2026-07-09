class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # my approach
        '''n = len(nums)
        out = [0] * n
        for i in range(n):
            product = 1  
            for j in range(n):  
                if j != i:
                    product = product * nums[j]
            out[i] = product
        return out'''

        # prefix - suffix approach (O(n))
        n = len(nums)
        prefix_product = [1] * n
        suffix_product = [1] * n
        out = [1] * n

        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]

        for i in range(n-2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]
            
        for i in range(n):    
            out[i] = prefix_product[i] * suffix_product[i]

        return out

            

