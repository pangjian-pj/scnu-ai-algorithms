def main():
    n=int(input())
    nums=list(map(int,input().split()))
    if n==1:
        print('0')
        return
    counts=0
    for i in range(1,n):
        if nums[i]>nums[i-1]:
            continue
        else:
            while nums[i]<=nums[i-1]:
                nums[i]=nums[i]+1
                counts=counts+1
    print(counts)

if __name__=='__main__':
    main()