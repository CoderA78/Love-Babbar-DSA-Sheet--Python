#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        if n==0 or n==1:
            return 
        a=[]
        j=0
        for i in range(len(arr)):
            if arr[i]>=0:
                a.append(arr[i])
                j+=1
        for i in range(len(arr)):
            if arr[i]<0:
                a.append(arr[i])
                j+=1
        # for i in range(len(arr)):
        #     a.append(arr[i])
        return a
