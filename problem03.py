# 背！！！
# 返回nums[left:right+1]区间内的最大连续子数组和
# 最大子数和可能出现在左区间、右区间以及跨越中点，左右区间的最大子数和递归求解，跨越中点的最大子数和以中点为界，分别向两边延伸求解
def max_subarray(nums,left,right):
    # 递归终止条件：当区间只剩下一个元素时。最大子数组只能是这个数组本身，直接返回该值
    if left == right:
        return nums[left]
    # 分治，划分左右两部分区间， //表示整除
    mid = (left + right) // 2
    # 递归求左区间的最大子数和
    left_max = max_subarray(nums,left,mid)
    # 递归求右区间的最大子数和
    right_max = max_subarray(nums,mid+1,right)
    # 以下是计算跨越中点的最大子数和
    # left_sum表示的是以mid结尾、向左延伸的最大连续子数和
    left_sum = float('-inf')
    tem = 0
    for i in range(mid,left-1,-1):
        tem = tem + nums[i]
        if tem > left_sum:
            left_sum = tem
    # right_sum表示的是以mid+1开始，向右延伸的最大连续子数和
    right_sum = float('-inf')
    tem = 0
    for i in range(mid+1, right+1):
        tem = tem + nums[i]
        if tem > right_sum:
            right_sum = tem
    # 跨越重点的最大子数和为上述两部份的和
    cross_sum = left_sum + right_sum
    # 在三种可能中取最大值
    return max(left_max,right_max,cross_sum)

n = int(input())
nums = list(map(int,input().split()))
print(max_subarray(nums,0,n-1))