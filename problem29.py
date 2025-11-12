def main():
    n = int(input())
    nums = list(map(int,input().split()))
    steps = 0
    if n == 1:
        print(0)
    else:
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                continue
            else:
                steps = steps+nums[i-1]-nums[i]+1
                nums[i] = nums[i-1]+1
        print(steps)

if __name__ == '__main__':
    main()
