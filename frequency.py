Write a program to find the frequency of a user-given character in a string.



n=input()
total={}
for i in n:
    if i in total:
        total[i]+=1
    else: 
        total[i]=1
print("count",str(total))


output:

dhivyaaa
count {'d':1,'h':1,'i':1,'v':1,'y':1,'a':3}

 to print with space:

     
string, character = map(str, input().split())
print(string.count(character))
