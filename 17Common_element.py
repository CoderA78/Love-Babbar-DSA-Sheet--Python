def commonElements (self,A, B, C, n1, n2, n3):
    i = j = k = 0
    result = []
    while i < n1 and j < n2 and k < n3:
        if A[i] == B[j] == C[k]:
            result.append(A[i])
            i += 1
            j += 1
            k += 1
        elif A[i] <= B[j] and A[i] <= C[k]:
            i += 1
        elif B[j] <= A[i] and B[j] <= C[k]:
            j += 1
        else:
            k += 1
    res=[]
    for i in range(len(result)):
        if result[i] in res:
            continue
        else:
            res.append(result[i])
    return res