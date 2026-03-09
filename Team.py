n=int(input())
b=0
for i in range(n):
  k=sum(list(map(int, input().split())))
  if k>=2: 
    b+=1
print(b)
