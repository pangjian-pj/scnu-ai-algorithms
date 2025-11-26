'''
   description: 给你一个整数n,返回和为n的完全平方数的最少数量。完全平方数是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
   method: 拉格朗日四平方和定理: 任何正整数都能表示成 4 个及以下的完全平方数组合。因此答案只可能是:1、2、3 或 4
   答案只可能是：
   1个完全平方数: 如果 n 本身是一个完全平方数，那么答案就是 1。
   2个完全平方数: 如果 n 可以表示为两个完全平方数之和
   3个完全平方数: 不是4^k*(8m+7) 型的数
   4个完全平方数: 是4^k*(8m+7) 型的数
'''

def main():
    import math
    n = int(input())
    if int(math.isqrt(n))**2 == n:
        print(1)
        return 
    for i in range(1,int(math.isqrt(n))+1):
        j = n - i*i
        if int(math.isqrt(j))**2 == j:
            print(2)
            return
    while n % 4 == 0:
        n //= 4
    if n % 8 == 7:
        print(4)
    else:
        print(3)

if __name__ == '__main__':
    main()