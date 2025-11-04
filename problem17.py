def main():
    n,k = input().split()
    n = int(n)
    k = int(k)
    nums = list(range(1,n+1))
    res = []
    def backtrack(start,path):
        if len(path)==k:
            res.append(path[:])
            return
        #  分支限界剪枝
        for i in range(start,n): 
            path.append(nums[i])
            backtrack(i+1,path)
            path.pop()
    backtrack(0,[])
    for path in res:
        print(*path,sep=' ')

if __name__ == '__main__':
    main()