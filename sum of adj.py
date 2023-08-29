n = int(input()) 
lst = list(map(int, input().split()))[:n] 
for i in range(n-1):
    print(sum(lst[i:i+2]),end=" ")
