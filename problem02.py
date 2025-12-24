# 先用字典统计每个数字出现的次数，然后再求其中出现次数最多的数字
n = int(input())
nums = list(map(int,input().split()))

# 初始化一个空字典
dicts = {}
# get函数：返回指定键的值，如果值不在字典中返回default值
for i in range(n):
    dicts[nums[i]] = dicts.get(nums[i], 0) + 1

# 通过max函数求最大值，使用key显示制定为字典的键，max函数的签名为max(iterable,key=None)，其中key表示的是一个函数
max_key = max(dicts,key=dicts.get)
print(max_key)