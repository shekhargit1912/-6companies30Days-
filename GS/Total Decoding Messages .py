#User function Template for python3

class Solution:
	def CountWays(self, str):
	    dp={len(str):1}
	    
	    
	    for i in range(len(str)-1,-1,-1):
	        if str[i]=="0":
	            dp[i]=0
	        else:
	            dp[i]=dp[i+1]
	            
	       
	        if (i+1<len(str) and (str[i]=="1" or str[i]=="2" and str[i+1] in "0123456")):
	            dp[i]+=dp[i+2]
	            
	            
	    return dp[0]
		# Code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.CountWays(str)
		print(ans)

# } Driver Code Ends
