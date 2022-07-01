t = int(input().strip())
print(type(t))
sum1=0
for _ in range(t):
    n = int(input().strip())
    for j in range(1,n):
        if j%3==0 or j%5==0:
            print(j)
            sum1+=j
    print(sum1)
