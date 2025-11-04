'''
    description: 给定一个非空的正整数数组 nums(nums.length < 5) ，请判断能否将这些数字分成元素和相等的两部分。
    method: 先对数组进行降序排序，然后依次按位对数组切片并求和判断即可。
'''

def main():
    nums = list(map(int,input().split()))
    nums.sort(reverse=True)
    for i in range(len(nums)):
        if sum(nums[:i+1])==sum(nums[i+1:]):
            print("true")
            return 
    print("false")
    return

if __name__ == '__main__':
    main()