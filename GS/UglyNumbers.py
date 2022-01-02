class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugl=[1]
        i=1
        u1,u2,u3=0,0,0
        while len(ugl)<n:
            by2=2*ugl[u1]
            by3=3*ugl[u2]
            by5=5*ugl[u3]
            umin=min(by2,by3,by5)
            ugl.append(umin)
            if umin==by2:
	            u1+=1
            if umin==by3:
                u2+=1
            if umin==by5:
                u3+=1
            i+=1
        return ugl[-1]
        
