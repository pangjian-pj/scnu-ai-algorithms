n, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(key=None,reverse=True)
print(nums[k-1])