def minJumps(arr, n):
    if n <= 1:
        return 0
    jumps = 0
    curr_end = 0
    max_reach = 0

    for i in range(n):
        if i > max_reach:
            return -1
        if i == n-1:
            return jumps
        max_reach = max(max_reach, i+arr[i])
        if i == curr_end:
            jumps += 1
            curr_end = max_reach

    return -1
