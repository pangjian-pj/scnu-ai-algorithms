'''
    经典背包问题
'''
def main():
    n, c = map(int,input().split())
    w_list = list(map(int, input().split()))
    v_list = list(map(int, input().split()))
    dp = [0]*(c+1)
    for i in range(n):
        w,v= w_list[i],v_list[i]
        for j in range(c,w-1,-1):
            new_val = dp[j-w]+v
            if new_val > dp[j]:
                dp[j] = new_val
    print(max(dp))

if __name__ == '__main__':
    main()

