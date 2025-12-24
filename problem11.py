def main():
    # python 中的字符串是不可变对象，因此要修改字符串中的字符，需要先把它用list转换成列表
    num=list(input())
    for i in range(len(num)):
        if num[i] == '6':
            num[i]='9'
            break
    print(*num,sep='')

if __name__=='__main__':
    main()