def main():
    n,k=map(int,input().split())
    res=[]
    for i in range(21):
        for j in range(35):
            for h in range(0,301,3):
                if i*5+j*3+h/3==n and i+j+h==k:
                    res.append([i,j,h])
    if len(res)==0:
        print(0)
    else:
        for i in range(len(res)):
            print(*res[i])

if __name__=='__main__':
    main()
