def main():
    n,k = input().split()
    n = int(n)
    k = int(k)
    res = []
    
    def backtrack(start, path:list):
        if len(path) == k:
            res.append(path[:])
            return
        
        for i in range(start, n+1):
            path.append(i)
            backtrack(i+1, path)
            path.pop()

    backtrack(1, [])

    print('[',end='')
    print(*res,sep=', ',end='')
    print(']')

if __name__ == "__main__":
    main()