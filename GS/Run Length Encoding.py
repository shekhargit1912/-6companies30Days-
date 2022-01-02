def encode(arr):
    
    cnt=0
    res=""
    i=0
    
    while i <len(arr):
        res+=arr[i]
        cnt=1
        while i+1<len(arr) and arr[i]==arr[i+1]:
            cnt+=1
            i+=1
            
        if i+1<len(arr) and arr[i]==arr[i+1]:
            continue
        else:
            i+=1
            
        res+=str(cnt)
        
    return (res)
