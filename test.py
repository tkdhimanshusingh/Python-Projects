A=[203,821,939]
Queries=[[1,2,472,0,0],[2,1,3,464,881]]
A[Queries[0][1]]=Queries[0][2]
s=0
for i in range(1,len(A)+1):
      if i>=Queries[1][1] and i<=Queries[1][2] and A[i-1]>=Queries[1][3] and A[i-1]<=Queries[1][4]:
          s+=A[i-1]
          print(A[i-1])
print(s)
print(A)
