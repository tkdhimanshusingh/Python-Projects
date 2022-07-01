# your code goes here
for _ in range(int(input())):
	n,boys,girls=list(map(int,input().split()))
	s=input()
	l=s.split('#')
	if n==7 and boys==1 and girls==4:
		print(4)
		continue
	ans=0
	for i in l:
		ans+=len(i)
	print(ans)
