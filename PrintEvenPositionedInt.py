# Input - 1 2 3 4 5
# Output - 2 4

numList=list(map(int, input().split()))
for index in range(1,len(numList),2):
    print(numList[index],end=" ")
