#Assignment : 4
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_table(n):
    table = [0] * (n + 1)
    table[0] = 0
    if n >= 1:
        table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


num = 10

print("Fibonacci using Memoization:", fib_memo(num))
print("Fibonacci using Tabulation:", fib_table(num))

#Output
'''Fibonacci using Memoization: 55
Fibonacci using Tabulation: 55'''