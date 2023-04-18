def overlappedInterval(self, Intervals):
    #Code here
    Intervals.sort(key=lambda x:x[0])
    
    merged=[]
    for interval in Intervals:
        if len(merged)==0 or merged[-1][1]<interval[0]:
            merged.append(interval)
        else:
            merged[-1][1]=max(merged[-1][1], interval[1])
    return merged