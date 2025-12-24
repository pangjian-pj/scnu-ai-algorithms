def main():
    nums = list(map(int,input().split()))
    target = int(input())
    res = 0
    # start表示当前处理到数组的第几个元素，path表示当前累计表达式的计算结果
    def backtrack(start:int,path:int):
        # 使用nonlocal才能在递归函数中修改外层函数的变量
        nonlocal res
        # 当已经对nums中的所有数字都选择过+或-后
        if start==len(nums):
            # 如果计算结果满足target，说明找到了一种合法方案
            if path == target:
                res = res+1
            return
        # 对每个数字，有选择+或-两种选择
        backtrack(start+1,path+nums[start])
        backtrack(start+1,path-nums[start])
    backtrack(0,0)
    print(res)

if __name__ == "__main__":
    main()


