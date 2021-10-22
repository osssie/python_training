n = int(input())
a = [[0 for i in range(n)] for j in range(n)]
i = 0
j = 0
x = 1
k = 0
while x <= n * n:
    a[i][j] = x
    if i != j:
        a[j][i] = (a[k][k] + (n - k * 2) * 2) * 2 - 4 - x
    if j != n - k - 1:
        j += 1
    elif i != n - k - 1:
        i += 1
    elif x != n * n:
        k += 1
        i = j = k
        x = a[k][k - 1]
    x += 1
for i in a: print(*i)
