import sys

dp = [[-1 for i in range(100)] for j in range(100)]

def matrix_chain_memoised(p, i, j):
    if i==j:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = sys.maxsize

    for k in range(i, j):
        dp[i][j] = min(dp[i][j], matrix_chain_memoised(p, i, k) 
        + matrix_chain_memoised(p, k+1, j) + p[i-1]*p[k]*p[j])

    return dp[i][j]


def matrix_chain_order(p, n):
    i = 1
    j = n-1
    return matrix_chain_memoised(p, i, j)

arr = [40, 20, 30, 10, 30]
n = len(arr)
print(matrix_chain_order(arr, n))
