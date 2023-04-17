class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        sum=0
        ans=0
        maxi=max(arr)
        if maxi<0:
            return maxi
        for i in range(len(arr)):
            sum+=arr[i]
            ans=max(ans, sum)
            if sum<0:
                sum=0
        return ans
            