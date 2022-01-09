#User function Template for python3

class Solution:
    def maxProfit(self, K, N, A):
        dp=[[0 for i in range(N+2)]for j in range(K+2)]
        
        for i in range(K+1):
            dp[i][0]=0
            
        for j in range(N+1):
            dp[0][j]=0
            
        for i in range(1,K+1):
            max1=-1*(1<<32)
            for j in range(1,N):
                max1=max(max1,dp[i-1][j-1]-A[j-1])
                dp[i][j]=max(dp[i][j-1],max1+A[j])
                
        return dp[K][N-1]
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        K = int(input())
        N = int(input())
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        print(ob.maxProfit(K, N, A))
# } Driver Code Ends
