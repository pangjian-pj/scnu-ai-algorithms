def main():
    n = int(input())
    res = 0
    # used数组用于记录每个数字是否已经被选入当前排列中
    used = [False]*(n+1)
    def backtrack(i):
        # 递归终止条件：遍历的数字大于n
        if i>n:
            nonlocal res
            res += 1
            return
        for x in range(1,n+1):
            if not used[x] and (x % i == 0 or i % x == 0):
                used[x] = True
                backtrack(i+1)
                used[x] = False
    backtrack(1)
    print(res)

if __name__ == "__main__":
    main()
