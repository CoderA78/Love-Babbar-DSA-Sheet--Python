class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        mini=arr[0]
        maxi=arr[n-1]
        res=maxi-mini
        for i in range(1,n):
            if arr[i]-k<0:
                continue
            maxi=max(arr[i-1]+k, arr[n-1]-k)
            mini=min(arr[i]-k,arr[0]+k)
            res=min(res,(maxi-mini))
        return res
            