def main():
    n=int(input())
    nums=list(map(int,input().split()))
    min_w=10001
    min_p=0
    for i in range(n):
        if nums[i]<min_w:
            min_w=nums[i]
            min_p=i
    print(min_p+1)

if __name__=='__main__':
    main()