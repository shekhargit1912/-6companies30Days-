#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        
        n=len(S)
        ans=[]
        stack=[]
        
        for i in range(n+1):
            stack.append(i+1)
            
            if i==n or S[i]=="I":
                while len(stack)!=0:
                    ans.append(chr(ord('0')+stack[-1]))
                    stack.pop()
                    
        return "".join(ans)
        
        
        # code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends
