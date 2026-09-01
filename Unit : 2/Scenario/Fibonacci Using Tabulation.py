#Unit 2 : Question 2
#Fibonacci Using Tabulation
def fibonacci(n):
    # making a table to store values
    table = [0] * (n + 1)

    if n >= 1:
        table[1] = 1

    for i in range(2, n + 1):
        # adding previous two values
        table[i] = table[i - 1] + table[i - 2]

    return table


n = int(input("Enter value of n: "))

result = fibonacci(n)

print("Fibonacci sequence is")
for num in result:
    print(num, end=" ")

#Output
'''Enter value of n: 8
Fibonacci sequence is
0 1 1 2 3 5 8 13 21'''