def main():
    s = input()
    res = []
    def backtrack(start:int,path:list):
        if start==len(s):
            res.append(path[:])
            return
        for i in range(start,len(s)):
            subStr = s[start:i+1]
            # 只在当前子串是回文串时才会继续探索
            if subStr==subStr[::-1]:
                path.append(subStr)
                backtrack(i+1,path)
                path.pop()
    backtrack(0,[])
    # 默认按字典序排序
    res.sort()
    print('[',end='')
    for i in res:
        print('['+', '.join(i)+']',end='')
        if res.index(i)!=len(res)-1:
            print(', ',end='')
        else:
            print(']')
    

if __name__ == "__main__":
    main()