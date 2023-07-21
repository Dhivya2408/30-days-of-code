Perform the function Int calculate(int m, int n). This function needs two positive integers. Calculate the sum of numbers between these two numbers that are divisible by 3 and 5.
Assumption
m > n > = 0

Example

Input:
m: 12
n: 50

Output:
90

Explanation
The numbers between 12 and 50 that are divisible by 3 and 5 are 15, 30, and 45. The sum of these numbers is 90.

Sample input:
m: 100
n: 160

Sample output:
405


output:
m = int(input())
n = int(input())
total=0
for i in range(m,n+1):
        if (i%3==0 and i%5==0):
            total= total + i
print(total)
