def findLongestConseqSubseq(self,arr, N):
    arr.sort()
    count=0
    nums=[]
    maxi=0
    nums.append(arr[0])
    
    for i in range(1,N):
        if arr[i]!=arr[i-1]:
            nums.append(arr[i])
    
    for i in range(len(nums)):
        if (i>0 and (nums[i]==nums[i-1]+1)):
            count+=1
        else:
            count=1
        maxi=max(maxi, count)
    return maxi