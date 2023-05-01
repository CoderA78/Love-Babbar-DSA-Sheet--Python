def countOccurence(self,arr,n,k):
    #Your code here
    d = {}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
        
    a = n//k
    c = 0
    for i in d:
        if d[i]>a:
            c+=1
    return c        