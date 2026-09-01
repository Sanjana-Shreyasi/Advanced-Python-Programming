#Unit 2 : Question 9
#0/1 Knapsack Problem
def knapsack(weights, values, capacity):
    n = len(weights)
    # making a table with all zeros first
    dp = [[0 for x in range(capacity + 1)] for y in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # either take the item or leave it
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    w = int(input("Enter weight of item " + str(i + 1) + ": "))
    v = int(input("Enter value of item " + str(i + 1) + ": "))
    weights.append(w)
    values.append(v)

capacity = int(input("Enter bag capacity: "))

result = knapsack(weights, values, capacity)

print("Maximum value that can be carried is", result)

#Output
'''Enter number of items: 3
Enter weight of item 1: 2
Enter value of item 1: 12
Enter weight of item 2: 1
Enter value of item 2: 10
Enter weight of item 3: 3
Enter value of item 3: 20
Enter bag capacity: 5
Maximum value that can be carried is 32'''