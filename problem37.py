'''
    dp[i][j] = True  表示 s[i..j] 是回文串
'''
def main():
    s = input()
    n = len(s)
    if n < 2:
        return s
    
    # dp[i][j] = s[i..j] 是否是回文
    dp = [[False]*n for _ in range(n)]

    start = 0
    max_len = 1

    # 单字符肯定是回文
    for i in range(n):
        dp[i][i] = True
    
    # 枚举右端点 j
    for j in range(1,n):
        # 枚举左端点 i
        for i in range(0,j):
            if s[i] == s[j]:
                if j-i<3:
                    dp[i][j]=True
                else:
                    dp[i][j]=dp[i+1][j-1]
            else:
                dp[i][j]=False

            if dp[i][j] and (j-i+1)>max_len:
                start = i
                max_len = j-i+1
    print(s[start:start+max_len])

if __name__ == '__main__':
    main()
