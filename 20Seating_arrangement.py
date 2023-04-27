def is_possible_to_get_seats(self, n : int, m : int, seats : List[int]) -> bool:
    c=0
    if m==1:
        if seats[0]==0:
            c+=1
        if c>=n:
            return True
        else:
            return False
            
    
    for i in range(m):
        if i==0 and seats[i]==0 and seats[i+1]==0:
            c+=1
            seats[i]=1
        elif i==m-1 and seats[i-1]==0 and seats[i]==0 :
            c+=1
            
        elif seats[i-1]==0 and seats[i]==0 and seats[i+1]==0 :
            c+=1
            seats[i]=1
    if c>=n:
        return True
    else:
        return False