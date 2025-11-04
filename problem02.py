n = int(input())
nums = list(map(int,input().split()))

dicts = {}
for i in range(n):
    dicts[nums[i]] = dicts.get(nums[i], 0) + 1

max_key = max(dicts,key=dicts.get)
print(max_key)