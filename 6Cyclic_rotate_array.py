def rotate( arr, n):
    B=1
    temp = arr[n-B:]
    for i in range(n-B-1, -1, -1):
        arr[i+B] = arr[i]
    for i in range(B):
        arr[i] = temp[i]
    return arr
    