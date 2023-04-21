class Solution:
    def nextPermutation(self, N, arr):
        pivot = -1
        for i in range(N-2, -1, -1):
            if arr[i] < arr[i+1]:
                pivot = i
                break
        
        # If there is no pivot element, reverse the array
        if pivot == -1:
            arr.reverse()
            return arr
        
        # Find the rightmost element that is greater than the pivot
        for i in range(N-1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break
        
        # Reverse the suffix starting at the element to the right of the pivot
        arr[pivot+1:] = reversed(arr[pivot+1:])
        
        return arr