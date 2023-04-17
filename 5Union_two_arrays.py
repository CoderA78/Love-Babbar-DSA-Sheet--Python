
class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        s=set()
        for i in range(len(a)):
            s.add(a[i])
        for i in range(len(b)):
            s.add(b[i])
        return len(s)