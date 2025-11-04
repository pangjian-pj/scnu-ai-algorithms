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