
def stockBuySell(self, A, n):
    #code here
    ans=[]
    for i in range(n-1):
        if A[i]<A[i+1]:
            ans.append((i,i+1))
    return ans
