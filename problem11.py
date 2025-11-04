def main():
    num = int(input())
    k = int(num / 1000)
    h = int((num - k*1000) /100)
    t = int((num - k*1000 - h*100) /10)
    o = num - k*1000 - h*100 - t*10
    sets = [k,h,t,o]
    results = []
    for s in sets:
        if s != 0:
            results.append(s)
    for i in range(len(results)):
        if results[i] == 6:
            results[i] = 9
            break
    print(*results,sep='')


if __name__ == "__main__":
    main()