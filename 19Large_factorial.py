def factorial(self,N):    
    if N==0:
        return [1]
    fact=1
    #ans=[]
    for i in range(1,N+1):
        fact=i*fact
    ans=[]

    while fact!=0:
        rem=fact%10
        fact=fact//10
        ans.insert(0,rem)
    #print(ans)
    return ans