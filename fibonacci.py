'''

Start with one Fibonacci sequence number, then calculate more from there.
Your input variable will contain a fibonacci sequence number. Your job is to calculate the next n digits.

Inputs
value1
The starting number

value2
n number to calculate after value1

Sample Test Cases

Small Number
value1 5
value2 2
output 8,13

Large Numbers
value1 34
value2 7
output 55,89,144,233,377,610,987

For the formulas refer the following blog:
https://apassionatechie.wordpress.com/2019/12/30/the-math-behind-fibonacci-numbers/

'''

import math

def findFibIndex(val):
    return round(2.078087 * math.log(val) + 1.672276)

def findFibIndexValue(index):
    golden_ratio = (1 + math.sqrt(5)) / 2
    return round(((golden_ratio ** index) - ((1 - golden_ratio) ** index)) / math.sqrt(5))

value1 = int(input())
value2 = int(input())
fib = []

index_value1 = findFibIndex(value1)
for i in range(value2):
    fib.append(findFibIndexValue(index_value1+(i+1)))

print(*fib, sep=',')
