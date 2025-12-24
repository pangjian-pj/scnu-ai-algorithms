'''
    description: 戳气球,动态规划
    method: dp[left][right] = 在开区间 (left, right) 内戳完所有气球能获得的最大硬币数
'''
def main():
    nums = list(map(int,input().split()))
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]

    # 三个for循环，分别对应区间长度，区间左端点和最后戳的气球
    # 枚举区间长度，为什么要从2开始，因为左右两边各加了一个哨兵，所以区间长度最初就是2
    for length in range(2,n):
        # 枚举区间左端点，这里区间长度是固定的
        for left in range(0, n-length):
            right = left + length
            # 枚举最后戳的气球
            for k in range(left+1,right):
                dp[left][right]=max(dp[left][right], 
                                    # dp[left][k]表示在区间(left,k)内，所有的气球都已经被戳完所获得的最大收益
                                    # nums[left]*nums[k]*nums[right]表示最后戳破k得到的收益
                                    # dp[k][right]表示在区间(k,right)内，所有的气球都已经被戳完所获得的最大收益
                                    dp[left][k]+nums[left]*nums[k]*nums[right]+dp[k][right] 
                                    )
    print(dp[0][n-1])

if __name__ == '__main__':
    main()

    
