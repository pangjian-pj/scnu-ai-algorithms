def main():
    s = input()
    res = []
    # start表示当前处理到字符串s的起始索引，path表示当前已经选择的回文子串序列
    def backtrack(start:int,path:list):
        # 递归终止条件，当start指向字符串末尾时，表示整个字符串已经被成功切分
        if start==len(s):
            res.append(path[:])
            return
        # 枚举所有以start为起点的子串
        for i in range(start,len(s)):
            subStr = s[start:i+1]
            # 只在当前子串是回文串时才会继续探索，subStr[::-1]表示字符串反转
            if subStr==subStr[::-1]:
                # 加入当前回文子串
                path.append(subStr)
                # 处理剩余字符串
                backtrack(i+1,path)
                # 撤销选择，尝试其他切分方式
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