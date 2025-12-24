def main():
    nums = list(map(int,input().split()))
    k = int(input())
    # 先求总和，如果总和不能被k整除，则说明不能划分为k个和相等的子集，立即返回
    total = sum(nums)
    if total%k != 0:
        print('false')
        return 
    # 先计算出每个子集的要达到的和
    target = total // k
    # 这里要倒序排序，先放大的数，再放小的数
    nums.sort(reverse=True)
    # buckets[i]表示第i个子集当前的和
    buckets = [0]*k
    # index表示的当前正在处理的数组元素下标
    def backtrack(index)->bool:
        # 递归终止条件：所有元素都已经放完了
        if index == len(nums):
            # 检查是否每个桶都恰好等于target
            return all(b==target for b in buckets)
        # num表示当前要放的数字
        num = nums[index]
        # 尝试把num放入到每一个桶中
        for i in range(k):
            # 如果放进去后不超过target，才允许继续
            if buckets[i]+num <= target:
                # 回溯三部曲：选择，递归处理下一个数字，撤销
                buckets[i] = buckets[i]+num
                if backtrack(index+1):
                    return True
                buckets[i] = buckets[i]-num
            # 这里表示的是，如果一个数字放入一个空桶中失败，那放入其他空桶中也一定会失败
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
