if __name__ == "__main__":
    dp = [0,1,2,4]
    t = int(input())

    for i in range(4,12):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    for _ in range(t):
        n = int(input())
        print(dp[n])



