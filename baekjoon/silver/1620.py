from sys import stdin

input = stdin.readline
dp = [0]*101
dp[1:3] =1,1,1

dp[4] = 2
dp[5] = 2

if __name__=="__main__":
    t = int(input())

    for i in range(6,102):
        dp[i] = dp[i-5] + dp[i-1]
    
    for _ in range(t):
        n = int(input())
        print(dp[n])