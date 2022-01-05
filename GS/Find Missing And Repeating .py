#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        map=dict()
        miss=0
        re=0
        for i in range(1,n+1):
            map[i]=0
        for ele in arr:
            map[ele]=map[ele]+1
        for i in map:
            if map[i]==0:
                re=i
            elif map[i]>1:
                miss=i
            
        return miss,re
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends
