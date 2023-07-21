The given function has a string (str) and two characters, ch1 and ch2. Execute the function in such a way that str returns to its original string, and all the events in ch1 are replaced by ch2, and vice versa.
Replacecharacter(Char str1, Char ch1, Int 1, Char ch2)

Assumption

This string has only alphabets that are in lower case.

Example

Input:
str: apples
ch1: a
ch2: p

Output:
paales

Explanation
All the ‘a’ in the string is replaced with ‘p’. And all the ‘p’s are replaced with ‘a’.


output:

s=input()
ch1=input()
ch2=input()
temp='0'
t1=s.replace(ch1,temp)
print(t1)
t2=t1.replace(ch2,ch1)
print(t2)
t3=t2.replace(temp,ch2)
print(t3)
