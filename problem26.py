'''
    description: 有一个非负整数数组nums ，最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。假设你总是可以到达数组的最后一个位置, 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
    method: 维护3个变量，其中farthest表示在当前位置当前最远能够跳到哪里，end表示跳跃能力的边界在哪里，当走到跳跃能力的边界时，则必须再起跳一次，jump表示跳跃的次数。
'''
def main():
    n = int(input())
    nums = list(map(int,input().split()))
    farthest = 0
    end = 0
    jump = 0
    for i in range(n-1):
        farthest = max(farthest, i+nums[i])
        if i == end:
            end = farthest
            jump = jump+1
    print(jump)

if __name__ == '__main__':
    main()