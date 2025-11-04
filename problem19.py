def main():
    nums = list(map(int,input().split()))
    k = int(input())
    total = sum(nums)
    if total%k != 0:
        print('false')
        return 
    target = total // k
    nums.sort(reverse=True)
    buckets = [0]*k
    def backtrack(index)->bool:
        if index == len(nums):
            return all(b==target for b in buckets)
        num = nums[index]
        for i in range(k):
            if buckets[i]+num <= target:
                buckets[i] = buckets[i]+num
                if backtrack(index+1):
                    return True
                buckets[i] = buckets[i]-num
            if buckets[i] == 0:
                break
        return False
    isOk = backtrack(0)
    if isOk:
        print('true')
    else:
        print('false')

if __name__ == '__main__':
    main()
