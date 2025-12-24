def main():
    prices = list(map(int,input().split()))
    m = prices.pop()
    specials = []
    for _ in range(m):
        sp = list(map(int,input().split()))
        specials.append(sp)
    needs = list(map(int,input().split()))
    n = len(prices)
    # cur_needs表示当前还需要购买的商品数量，使用tuple是为了可哈希，不可变
    def dfs(cur_needs:tuple):
        cur_needs = list(cur_needs)
        # 原价购买的价格是当前状态的一个上限，就是最贵也就是原价购买了
        cost = sum(cur_needs[i]*prices[i] for i in range(n))
        # 尝试使用每一种礼包，看看是否更优惠
        for sp in specials:
            new_needs = []
            # 对每种商品
            for i in range(n):
                # 如果礼包中商品数量大于当前所需的数量，那该礼包就不可用
                if sp[i] > cur_needs[i]:
                    break
                # 可用的情况下，计算使用该礼包后的剩余需要购买的数量
                new_needs.append(cur_needs[i]-sp[i])
            # 这里用的是for-else结构，else只有在for循环没有被break打断时才执行
            else:
                # sp[-1]+dfs(tuple(new_needs))表示使用当前礼包，剩下的需求继续递归求解
                cost = min(cost, sp[-1]+dfs(tuple(new_needs)))
        return cost
    print(dfs(tuple(needs)))

if __name__ == '__main__':
    main()