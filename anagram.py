Input:

Input 1: 1st string
Input 2: 2nd string

Output:
(If they are anagrams, the function will return ‘yes’. Otherwise, it will return ‘no’.)

Example

Input 1: Listen
Input 2: Silent

Output:
Yes

Explanation

Listen and Silent are anagrams (an anagram is a word formed by rearranging the letters of the other word).


output:

s1=input()
s2=input()
print(s1)
print(s2)
temp1=sorted(s1)
print(temp1)
temp2=sorted(s2)
print(temp2)
if temp1==temp2:
    print("yes")
else:
    print("no")
