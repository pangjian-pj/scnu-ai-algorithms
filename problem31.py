def main():
    k,n = map(int,input().split())
    res = []
    def backtrack(start:int,path:list):
        if sum(path)==n and len(path)==k:
            res.append(path[:])
            return
        elif len(path)>=k or sum(path)>n:
            return
        for i in range(start,10):
            path.append(i)
            backtrack(i+1,path)
            path.pop()
    backtrack(1,[])
    res.sort(reverse=True)
    for r in res:
        print(*r)
    if not res:
        print(0)

if __name__ == '__main__':
    main()
