def main():
    nums = list(map(int,input().split()))
    target = int(input())
    res = 0
    def backtrack(start:int,path:int):
        nonlocal res
        if start==len(nums):
            if path == target:
                res = res+1
            return
        backtrack(start+1,path+nums[start])
        backtrack(start+1,path-nums[start])
    backtrack(0,0)
    print(res)

if __name__ == "__main__":
    main()


