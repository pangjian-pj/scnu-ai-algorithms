'''
    description: 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。给定一个代表每个房屋存放金额的非负整数数组，计算你不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
    method: 每个房屋有两种状态，偷或者不偷，偷的话，用dp[i]表示如果偷当前房屋能的得到的最高金额，偷则是当前dp[i]=dp[i-2]+nums[i-1],不偷则是dp[i]=dp[i-1]，取最大值，
'''
def main():
    nums = list(map(int,input().split()))
    dp = [0]*(len(nums)+1)
    dp[1] = nums[0]
    for i in range(2,len(nums)+1):
        dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
    print(max(dp))

if __name__ == '__main__':
    main()
