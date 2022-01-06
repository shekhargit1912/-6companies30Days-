class Solution:
    def help(self,s,n,dp):
        if s==n:
            return 1
        if s>=n:
            return 0
        if dp[s]!=-1:
            return dp[s]
        ans= self.help(s+1,n,dp)+self.help(s+2,n,dp)
        dp[s]=ans
        return dp[s]
    
    def climbStairs(self, n: int) -> int:
        dp=[-1 for i in range(n+1)]
        return self.help(0,n,dp)
        
