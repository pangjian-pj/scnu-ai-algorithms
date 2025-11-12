def main():
    n = int(input())
    a = list(map(int,input().split()))
    w_max = 100000
    w_i = -1
    for i in range(n):
        if a[i]< w_max:
            w_max = a[i]
            w_i = i
    print(w_i+1)

if __name__ == '__main__':
    main()