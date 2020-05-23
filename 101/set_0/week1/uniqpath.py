def uniq_path(row=2, col=3):
    dp = [[1]*col for i in range(row)]
    print(dp)
    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp)

uniq_path()