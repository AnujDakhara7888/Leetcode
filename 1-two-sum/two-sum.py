class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        num_map={}
        for i,x in enumerate(nums):
            remaining = target-x
            if remaining in num_map:
                return [num_map[remaining],i]
            num_map[x]=i




        