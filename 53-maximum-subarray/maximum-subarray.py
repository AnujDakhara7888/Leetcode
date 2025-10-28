class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalnow=nums[0]
        totalglobal=nums[0]
        for i in range(1, len(nums)):
            totalnow = max(nums[i],totalnow+nums[i])
            totalglobal = max(totalglobal,totalnow)
        
        return totalglobal
            
            
            
        