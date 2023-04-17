def getMinMax( a, n):
    mini=10**10
    maxi=-10**10
    for i in range(n):
        maxi=max(maxi,a[i])
        mini=min(mini,a[i])
    return mini, maxi
    