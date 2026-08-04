#Assignment : 5

def find_lcs(a, b):
    len_a = len(a)
    len_b = len(b)

    dp = [[0] * (len_b + 1) for x in range(len_a + 1)]

    for row in range(1, len_a + 1):
        for col in range(1, len_b + 1):
            if a[row - 1] == b[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                if dp[row - 1][col] > dp[row][col - 1]:
                    dp[row][col] = dp[row - 1][col]
                else:
                    dp[row][col] = dp[row][col - 1]

    result = ""
    row = len_a
    col = len_b

    while row > 0 and col > 0:
        if a[row - 1] == b[col - 1]:
            result = a[row - 1] + result
            row -= 1
            col -= 1
        elif dp[row - 1][col] > dp[row][col - 1]:
            row -= 1
        else:
            col -= 1

    return result, dp[len_a][len_b]


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

subseq, length = find_lcs(s1, s2)

print("\nLCS String:", subseq)
print("LCS Length:", length)

#Output
'''Enter first string: ABCBDAB
Enter second string: BDCABA
LCS String: BCBA
LCS Length: 4'''