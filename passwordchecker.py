Write a function CheckPassword(str) which will accept the string as an argument or parameter and validates the password. It will return 1 if the conditions are satisfied else it’ll return 0?

The password is valid if it satisfies the below conditions:

It should contain at least 4 characters.
At least 1 numeric digit should be present.
1 Capital letter should be there.
Password should not contain space or slash.
The starting character should not be a number.



coding:

def validatepassword(s,l):
    if l<4:
        return 0
    caps=0
    num=0
    for i in range(l):
        if s[0].isdigit():
            return 0
        if s[i]==' ' and s[i]=='/':
            return 0
        if s[i]>='A' and s[i]<='Z':
            caps+=1
        if s[i].isdigit():
            num+=1
    if caps>0 and num>0:
        return 1
    else:
        return 0
