'''
    description: 有一个非负整数数组nums ，最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。假设你总是可以到达数组的最后一个位置, 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
    method: 维护3个变量，其中farthest表示在当前位置当前最远能够跳到哪里，end表示跳跃能力的边界在哪里，当走到跳跃能力的边界时，则必须再起跳一次，jump表示跳跃的次数。
'''
def main():
    n = int(input())
    nums = list(map(int,input().split()))
    # farthest表示当前这一跳范围内，能够到达的最远下标
    farthest = 0
    # end表示当前跳跃次数jump所能覆盖的最远边界
    end = 0
    # jump表示跳跃次数
    jump = 0
    # 这里只遍历到n-1，因为到最后一个位置就不起跳了
    for i in range(n-1):
        # 计算从当前位置i出发，最远能跳到哪里
        farthest = max(farthest, i+nums[i])
        # 已经遍历完当前跳跃次数jump所能覆盖的所有位置了，此时必须再跳一次，否则无法继续前进
        if i == end:
            # 将下一跳的覆盖范围更新为farthest
            end = farthest
            jump = jump+1
    print(jump)

if __name__ == '__main__':
    main()