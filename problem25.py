def main():
    s=list(input())
    stack=[]
    queue=[]
    for i in range(len(s)):
        if s[i]!=')':
            stack.append(s[i])
        else:
            while True:
                temp=stack[-1]
                if temp!='(':
                    queue.append(temp)
                    stack.pop()
                else:
                    stack.pop()
                    for i in range(len(queue)):
                        stack.append(queue[i])
                    queue.clear()
                    break
    print("".join(stack))

if __name__=='__main__':
    main()