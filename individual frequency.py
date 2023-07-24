from collections import Counter
a= list(map(str, input().split()))
b=input()
temp = Counter(a) 
print(temp[b])
