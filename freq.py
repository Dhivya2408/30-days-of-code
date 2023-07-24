n=input()
total={}
for i in n:
    if i in total:
        total[i]+=1;
    else:
        total[i]=1;
print("count",str(total))
