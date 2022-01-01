#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        
        start=0
        end=0
        count=0
        prod=1
        
        while end<n:
            prod*=a[end]
            
            while start <n and prod>=k:
                prod/=a[start]
                start+=1
                
            if prod<k:
                count+=(end-start+1)
                
            end+=1
        return count
        
        
        #Code here
    
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
