def main():
    n = int(input())
    res = []

    def backtrack(cur, left, right):
        '''
        cur表示当前已构造好的括号字符串，left表示已使用的左括号数量，right表示已使用的右括号数量
        '''
        # 递归终止条件：一个合法括号串的长度一定是2n，当构造完成时，将当前字符串加入结果并结束当前的递归分支
        if len(cur) == 2*n:
            res.append(cur)
            return 
        # 添加左括号的条件：左括号最多只能使用n个
        if left < n:
            backtrack(cur+"(",left+1,right)
        # 添加右扩号的条件：右括号数量不能多过左括号
        if right < left:
            backtrack(cur+")",left,right+1)
    
    backtrack("",0,0)
    print("["+", ".join(res)+"]")

if __name__ == "__main__":
    main()