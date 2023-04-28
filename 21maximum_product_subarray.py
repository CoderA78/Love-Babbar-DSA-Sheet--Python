def maxProduct(self,arr, n):
    ans = arr[0]
    ma, mi = ans, ans
    
    for i in range(1,n):
        if arr[i] < 0:
            temp = ma
            ma = mi
            mi = temp
        ma = max(arr[i], ma*arr[i])
        mi = min(arr[i], mi*arr[i])
        ans = max(ans, ma)
    return ans