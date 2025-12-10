def sub_sum(nums,start,end):
    res = 0
    for i in range(start,end+1):
        res = res + nums[i]
    return res

def main():
    n = int(input())
    nums = list(map(int,input().split()))
    dp = [0]*n
    dp[0] = nums[0]
    for i in range(1,n):
        max_sub_sum = 0
        for j in range(i+1):
            s_sum = sub_sum(nums,j,i)
            if s_sum > max_sub_sum:
                max_sub_sum =s_sum
        dp[i]=max_sub_sum
    print(max(dp))

if __name__ == '__main__':
    main()
