def maxSubArraySum(self,arr,N):
    sum=0
    ans=0
    maxi=max(arr)
    if maxi<0:
        return maxi
    for i in range(len(arr)):
        sum+=arr[i]
        ans=max(sum,ans)
        if sum<0:
            sum=0
    return ans
            