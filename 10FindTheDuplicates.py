def duplicates(self, arr, n): 
    # code here
    map=dict()
    for i in range(n):
        if arr[i] in map.keys():
            map[arr[i]]+=1
        else:
            map[arr[i]]=1
    array=[]
    for key, value in map.items():
        if value>=2:
            array.append(key)
    array.sort()
    if len(array)>0:
        return array
    return [-1]
