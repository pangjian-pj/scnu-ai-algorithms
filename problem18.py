def main():
    prices = list(map(int,input().split()))
    m = prices.pop()
    specials = []
    for _ in range(m):
        sp = list(map(int,input().split()))
        specials.append(sp)
    needs = list(map(int,input().split()))
    n = len(prices)
    def dfs(cur_needs):
        cur_needs = list(cur_needs)
        cost = sum(cur_needs[i]*prices[i] for i in range(n))
        for sp in specials:
            new_needs = []
            for i in range(n):
                if sp[i] > cur_needs[i]:
                    break
                new_needs.append(cur_needs[i]-sp[i])
            else:
                cost = min(cost, sp[-1]+dfs(tuple(new_needs)))
        return cost
    print(dfs(tuple(needs)))

if __name__ == '__main__':
    main()