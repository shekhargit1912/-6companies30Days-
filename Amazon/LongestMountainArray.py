class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res=0
        
        for ind in range(1,len(arr)-1):
            #cuase first and last valu are not the peak values
            if arr[ind-1]<arr[ind]>arr[ind+1]:
                #peak value
                l=ind
                r=ind
                
                
                while l >0and arr[l]>arr[l-1]:
                    l-=1
                    
                while r+1<len(arr) and arr[r]>arr[r+1]:
                    r+=1
                    
                    
                res=max(res,(r-l+1))
                
        return res
