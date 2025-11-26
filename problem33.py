'''
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

如果直接双重循环+remove操作会超时，需要先排序再使用双指针法
'''

def main():
    g = list(map(int,input().split()))
    s = list(map(int,input().split()))
    g.sort()
    s.sort()
    i=j=res = 0
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            res += 1
            i += 1
            j += 1
        else:
            j += 1
    print(res)

if __name__ == '__main__':
    main()