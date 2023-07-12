# Traditional method 
lst = []
n = int(input())
for i in range(0,n): 
    val = int(input()) 
    lst.append(val) 
    
print(lst)

# Efficient method 
n = int(input())
lst = list(map(int, input().split()))[:n]
print(lst)

# Appending values 
n = int(input())
lst = list(map(int, input().split()))[:n]
print(lst)
lst.append(10)
print(lst)
