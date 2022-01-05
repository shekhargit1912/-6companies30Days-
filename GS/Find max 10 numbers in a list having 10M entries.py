#find n largest element in the list


def Nlarge(li,n):
    
    final=[]
    for i in range(0,n):
        max1=0
        
        for j in range(len(li)):
            if li[j]>max1:
                max1=li[j]
                
        li.remove(max1)
        final.append(max1)
    return final



li=[2,3,85,41,3]
n=2
ans=Nlarge(li,n)
print(ans)
