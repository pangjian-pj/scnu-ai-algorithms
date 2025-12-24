# 背！这道题主要是用到了一个Counter去做计数器，然后要记住它的一个思想，使用坏字符去做分割，然后对每一段递归求解
from collections import Counter

def longestSubstring(s,k):
    # 递归终止条件：如果一个字符串本身长度已经小于k了，那就已经没有可满足条件的子串了
    if len(s) < k:
        return 0
    # Counter是一个哈希表计数工具，输入一个字符串，可以返回每个元素出现的次数，counter对象本质是一个字典
    freq = Counter(s)

    for ch in freq:
        # 如果一个字符在整个字符串中出现次数小于k，那么它不可能出现在任何合法子串中，
        if freq[ch] < k:
            # 因此我们可以用这个坏字符把字符串切开，对每一段递归求解
            parts = s.split(ch)
            return max(longestSubstring(p,k) for p in parts)
    # 如果不存在坏字符，则说明整个字符串都是一个合格的子串
    return len(s)

s, k = map(str,input().split())
k = int(k)

print(longestSubstring(s,k))