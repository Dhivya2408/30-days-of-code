# Sum of Adjacent Elements
n= int(input())
lst = list(map(int, input().split()))[:n]
for i in range(0,n-1):
   print(lst[i]+lst[i+1])
