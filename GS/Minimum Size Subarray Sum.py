class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        ans=len(nums)+1
        left=0
        sum1=0
        
        for i in range(n):
            sum1+=nums[i]
            while sum1>=target:
                ans=min(ans,i+1-left)
                sum1=sum1-nums[left]
                left+=1
                
                
        if ans==len(nums)+1:
            return 0
        
        return ans
        
