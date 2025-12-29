#동전0

N, K = map(int,input().split())

arr = []

for i in range(N):
    a = int(input())
    arr.append(a)
    
arr.reverse()
    
sum = 0
for j in range(len(arr)):
    v = K // arr[j]
    K = K % arr[j]
    sum += v
    
print(sum)
