def sub_sum(nums,start,end):
    res=0
    for i in range(start,end+1):
        res=res+nums[i]
    return res

def main():
    n=int(input())
    nums=list(map(int,input().split()))
    dp=[0]*n
    dp[0]=nums[0]
    for i in range(n):
        max_sum=0
        for j in range(i+1):
            temp_sum=sub_sum(nums,j,i)
            if temp_sum>max_sum:
                max_sum=temp_sum
        dp[i]=max_sum
    print(max(dp))

if __name__=='__main__':
    main()
