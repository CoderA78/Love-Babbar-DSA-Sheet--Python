def subArrayExists(self,arr,n):
    curr_sum=0

    d={}

    max_len=0

    for i in range(n):

        curr_sum=curr_sum+arr[i]

        if curr_sum==0 or curr_sum in d:

            return True

        d[curr_sum]=i

    return False