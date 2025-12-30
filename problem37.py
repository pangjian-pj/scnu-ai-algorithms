'''
    dp[i][j] = True  表示 s[i..j] 是回文串
'''
def main():
    s = input()
    n = len(s)
    if n < 2:
        return s
    
    # dp[i][j] = True 表示s[i..j] 是否是回文
    dp = [[False]*n for _ in range(n)]

    # 最长回文子串的起始位置
    start = 0
    # 当前找到的最长回文子串长度
    max_len = 1

    # 单字符肯定是回文
    for i in range(n):
        dp[i][i] = True
    
    # 枚举右端点 j
    for j in range(1,n):
        # 枚举左端点 i
        for i in range(0,j):
            if s[i] == s[j]:
                # 对于长度为2或3的子串，只要首尾相等，一定是回文
                if j-i<3:
                    dp[i][j]=True
                else:
                    dp[i][j]=dp[i+1][j-1]
            else:
                dp[i][j]=False
            # 如果当前子串是回文，且长度大于之前记录的最大长度，则更新答案
            if dp[i][j] and (j-i+1)>max_len:
                start = i
                max_len = j-i+1
    print(s[start:start+max_len])

if __name__ == '__main__':
    main()
