"""
Problem 4

Write a function that meets the following specification. Hint: there exists a greedy algorithm that provides an optimal solution to this problem.

def solve(s):
 
    s: positive integer, what the sum should add up to
    Solves the following optimization problem:
        x1 + x2 + x3 + x4 is minimized 
        subject to the constraint x1*25 + x2*10 + x3*5 + x4 = s
        and that x1, x2, x3, x4 are non-negative integers.


"""

def solve(s):
    multipliers = []
    remain = s
    for i in s:
        if i <= remain:
            mult = remain // i
            multipliers.append(mult)
            remain -= i * mult
        else:
            multipliers.append(0)
    sum1 = 0
    for j in range(len(multipliers)):
        sum1 += L[j]*multipliers[j]
    if sum1 == s:
        return sum(multipliers)
    else:
        return 'no solution'