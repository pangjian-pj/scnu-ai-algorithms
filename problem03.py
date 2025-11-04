def max_subarray(nums,left,right):
    if left == right:
        return nums[left]
    mid = (left + right) // 2
    left_max = max_subarray(nums,left,mid)
    right_max = max_subarray(nums,mid+1,right)
    left_sum = float('-inf')
    tem = 0
    for i in range(mid,left-1,-1):
        tem = tem + nums[i]
        if tem > left_sum:
            left_sum = tem
    right_sum = float('-inf')
    tem = 0
    for i in range(mid+1, right+1):
        tem = tem + nums[i]
        if tem > right_sum:
            right_sum = tem
    cross_sum = left_sum + right_sum
    return max(left_max,right_max,cross_sum)

n = int(input())
nums = list(map(int,input().split()))
print(max_subarray(nums,0,n-1))