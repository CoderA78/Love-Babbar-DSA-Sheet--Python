class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def merge(self,arr, temp_arr, left, mid, right):
        i = left     
        j = mid + 1 
        k = left     
        inv_count = 0 
      
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid-i + 1)  
                j += 1
            k += 1
      
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
      
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1
      
        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]
              
        return inv_count
      
    def merge_sort(self,arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += self.merge_sort(arr, temp_arr, left, mid)
            inv_count += self.merge_sort(arr, temp_arr, mid + 1, right)
            inv_count += self.merge(arr, temp_arr, left, mid, right)
        return inv_count
  
    def inversionCount(self, arr, n):
        # Your Code Here
        # n = len(arr)
        temp_arr = [0]*n
        return self.merge_sort(arr, temp_arr, 0, n-1)
                    