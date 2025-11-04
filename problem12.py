def main():
    n = int(input())
    res = []

    def backtrack(cur, left, right):
        if len(cur) == 2*n:
            res.append(cur)
            return 
        if left < n:
            backtrack(cur+"(",left+1,right)
        if right < left:
            backtrack(cur+")",left,right+1)
    
    backtrack("",0,0)
    print("["+", ".join(res)+"]")

if __name__ == "__main__":
    main()