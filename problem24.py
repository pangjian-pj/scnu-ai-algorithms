def main():
    n=int(input())
    nums=list(map(int,input().split()))
    res=[]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k]==0:
                    temp=[nums[i],nums[j],nums[k]]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
    res.sort()
    print('[',end='')
    for i in range(len(res)):
        temp=res[i]
        print('[',end='')
        for j in range(3):
            print(temp[j],end='')
            if j!=2:
                print(',',end='')
        print(']',end='')
        if i!=len(res)-1:
            print(',',end='')
    print(']')

if __name__=='__main__':
    main()