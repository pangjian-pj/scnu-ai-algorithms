def sub_sum(nums,start,end):
    res = 0
    for i in range(start,end+1):
        res = res + nums[i]
    return res

def main():
    n = int(input())
    nums = list(map(int,input().split()))
    # dp[i]表示第i个元素结尾的最大子数和
    dp = [0]*n
    # 初始化：第一个元素的最大子数和就是它自己
    dp[0] = nums[0]
    # 先遍历所有数字
    for i in range(1,n):
        # 记录以第i个元素结尾的最大子数和
        max_sub_sum = 0
        # 再遍历所有可能的起始位置
        for j in range(i+1):
            s_sum = sub_sum(nums,j,i)
            if s_sum > max_sub_sum:
                max_sub_sum =s_sum
        dp[i]=max_sub_sum
    print(max(dp))

if __name__ == '__main__':
    main()
