from collections import Counter

def longestSubstring(s,k):
    if len(s) < k:
        return 0
    
    freq = Counter(s)

    for ch in freq:
        if freq[ch] < k:
            parts = s.split(ch)
            return max(longestSubstring(p,k) for p in parts)
    return len(s)

s, k = map(str,input().split())
k = int(k)

print(longestSubstring(s,k))