def main():
    nums = list(map(int,input().split()))
    l = len(nums)
    res = []

    def backtrack(i,cur_xor):
        if i==l:
            res.append(cur_xor)
            return
        backtrack(i+1,cur_xor)
        backtrack(i+1,cur_xor^nums[i])

    backtrack(0,0)
    print(sum(res))


if __name__ == "__main__":
    main()