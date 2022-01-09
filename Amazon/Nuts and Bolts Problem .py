#User function Template for python3
class Solution:

	def matchPairs(self,nuts, bolts, n):
	    map={}
	    
	    for i in range(n):
	        map[bolts[i]]=i
	        
	    for i in range(n):
	        if nuts[i] in map:
	            bolts[i]=nuts[i]
	            
		# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(nuts, bolts, n)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
