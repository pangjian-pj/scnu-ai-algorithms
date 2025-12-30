# 第一题
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def Max_BT(nums):
    if not nums:
        return None
    Max_val=max(nums)
    Max_index=nums.index(Max_val)
    root=TreeNode(Max_val)
    root.left=Max_BT(nums[:Max_index])
    root.right=Max_BT(nums[Max_index+1:])
    return root

def preOrder(root):
    if not root:
        return 'null'
    if not root.left and not root.right:
        return root.val
    left_str = preOrder(root.left)
    right_str = preOrder(root.right)
    return f"{root.val} {left_str} {right_str}"

nums = list(map(int,input().split()))
root = Max_BT(nums)
print(preOrder(root))

# # 第二题
# n = int(input())
# nums = list(map(int,input().split()))

# dicts = {}
# for i in range(n):
#     dicts[nums[i]] = dicts.get(nums[i], 0) + 1

# max_key = max(dicts,key=dicts.get)
# print(max_key)

# # 第三题
# def max_subarray(nums,left,right):
#     if left == right:
#         return nums[left]
#     mid = (left + right) // 2
#     left_max = max_subarray(nums,left,mid)
#     right_max = max_subarray(nums,mid+1,right)
#     left_sum = float('-inf')
#     tem = 0
#     for i in range(mid,left-1,-1):
#         tem = tem + nums[i]
#         if tem > left_sum:
#             left_sum = tem
#     right_sum = float('-inf')
#     tem = 0
#     for i in range(mid+1, right+1):
#         tem = tem + nums[i]
#         if tem > right_sum:
#             right_sum = tem
#     cross_sum = left_sum + right_sum
#     return max(left_max,right_max,cross_sum)

# n = int(input())
# nums = list(map(int,input().split()))
# print(max_subarray(nums,0,n-1))

# # 第四题
# n, k = map(int,input().split())
# nums = list(map(int,input().split()))

# nums.sort()
# print(' '.join(map(str,nums[:k])))

# # 第五题
# n, k = map(int, input().split())
# nums = list(map(int, input().split()))

# nums.sort(key=None,reverse=True)
# print(nums[k-1])

# # 第六题
# from collections import Counter

# def longestSubstring(s,k):
#     if len(s) < k:
#         return 0
#     freq = Counter(s)

#     for ch in freq:
#         if freq[ch] < k:
#             parts = s.split(ch)
#             return max(longestSubstring(p,k) for p in parts)
#     return len(s)

# s, k = map(str,input().split())
# k = int(k)

# print(longestSubstring(s,k))

# # 第七题
# '''
# 偷懒版
# nums = list(map(int,input().split()))
# nums.sort()
# print(*nums, sep=" ")
# '''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next 

# def merge(l1, l2):
#     dummy = ListNode(0)
#     cur = dummy
#     while l1 and l2:
#         if l1.val < l2.val:
#             cur.next = l1
#             l1 = l1.next
#         else:
#             cur.next = l2
#             l2 = l2.next
#         cur = cur.next
#     cur.next = l1 if l1 else l2
#     return dummy.next

# def sortList(head):
#     if not head or not head.next:
#         return head
#     slow, fast = head, head.next
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     mid = slow.next
#     slow.next = None
#     left = sortList(head)
#     right = sortList(mid)
#     return merge(left,right)

# nums = list(map(int,input().split()))
# dummy = ListNode(0)
# cur = dummy
# for n in nums:
#     cur.next = ListNode(n)
#     cur = cur.next
# head = dummy.next

# head =sortList(head)

# cur = head
# res = []
# while cur:
#     res.append(str(cur.val))
#     cur = cur.next

# print(' '.join(res))

# # 第八题
# bills = list(map(int,input().split()))
# changes = True
# wallet = {"5":0,"10":0,"20":0}
# for b in bills:
#     if b == 5:
#         wallet["5"] = wallet["5"] + 1
#     elif b == 10:
#         if wallet["5"] >= 1 :
#             wallet["10"] = wallet["10"] + 1
#             wallet["5"] = wallet["5"] - 1
#         else:
#             changes = False
#             break
#     else:
#         if wallet["5"] >= 3 :
#             wallet["20"] = wallet["20"] + 1
#             wallet["5"] = wallet["5"] - 3
#         elif wallet["10"] >= 1 and wallet["5"] >= 1:
#             wallet["20"] = wallet["20"] + 1
#             wallet["5"] = wallet["5"] - 1
#             wallet["10"] = wallet["10"] - 1
#         else:
#             changes = False
#             break
# if changes:
#     print("true")
# else:
#     print("false")

# # 第九题
# def coin_change(n:int)->list:
#     coins = [2, 5, 7]
#     INF = n + 1
#     dp = [INF] * (n+1)
#     dp[0] = 0
#     for i in range(1, n+1):
#         for c in coins:
#             if i >= c:
#                 dp[i] = min(dp[i], dp[i-c]+1)
#     return dp

# n = int(input())
# dp = coin_change(n)
# if dp[n] == n+1:
#     print("-1")
# else:
#     print(dp[n])

# # 第十题
# def main():
#     m,n=input().split()
#     m=int(m)
#     n=int(n)
#     dp=[[0]*(n+1) for _ in range(m+1)]
#     for i in range(1,m+1):
#         dp[i][1]=1
#     for j in range(1,n+1):
#         dp[1][j]=1
#     dp[1][1]=0
#     for i in range(2,m+1):
#         for j in range(2,n+1):
#             dp[i][j]=dp[i-1][j]+dp[i][j-1]
#     print(dp[m][n])

# # 十一题
# def main():
#     num=list(input())
#     for i in range(len(num)):
#         if num[i] == '6':
#             num[i]='9'
#             break
#     print(*num,sep='')

# # 十二题
# def main():
#     n = int(input())
#     res = []

#     def backtrack(cur, left, right):
#         if len(cur) == 2*n:
#             res.append(cur)
#             return 
#         if left < n:
#             backtrack(cur+"(",left+1,right)
#         if right < left:
#             backtrack(cur+")",left,right+1)
    
#     backtrack("",0,0)
#     print("["+", ".join(res)+"]")

# # 十三题
# def main():
#     n,k = input().split()
#     n = int(n)
#     k = int(k)
#     res = []
    
#     def backtrack(start, path:list):
#         if len(path) == k:
#             res.append(path[:])
#             return
        
#         for i in range(start, n+1):
#             path.append(i)
#             backtrack(i+1, path)
#             path.pop()

#     backtrack(1, [])

#     print('[',end='')
#     print(*res,sep=', ',end='')
#     print(']')

# # 十四题
# def main():
#     nums = list(map(int, input().split()))
#     n = len(nums)

#     or_val = 0
#     for x in nums:
#         or_val =or_val|x 

#     print(or_val * (1 << (n - 1)))

# # 十五题
# def main():
#     s = input()
#     res = []
#     def backtrack(start:int,path:list):
#         if start==len(s):
#             res.append(path[:])
#             return
#         for i in range(start,len(s)):
#             subStr = s[start:i+1]
#             if subStr==subStr[::-1]:
#                 path.append(subStr)
#                 backtrack(i+1,path)
#                 path.pop()
#     backtrack(0,[])
#     res.sort()
#     print('[',end='')
#     for i in res:
#         print('['+', '.join(i)+']',end='')
#         if res.index(i)!=len(res)-1:
#             print(', ',end='')
#         else:
#             print(']')
    

# # 十六题
# def main():
#     nums = list(map(int,input().split()))
#     target = int(input())
#     res = 0
#     def backtrack(start:int,path:int):
#         nonlocal res
#         if start==len(nums):
#             if path == target:
#                 res = res+1
#             return
#         backtrack(start+1,path+nums[start])
#         backtrack(start+1,path-nums[start])
#     backtrack(0,0)
#     print(res)

# # 十七题
# def main():
#     n,k = input().split()
#     n = int(n)
#     k = int(k)
#     nums = list(range(1,n+1))
#     res = []
#     def backtrack(start,path):
#         if len(path)==k:
#             res.append(path[:])
#             return
#         for i in range(start,n): 
#             path.append(nums[i])
#             backtrack(i+1,path)
#             path.pop()
#     backtrack(0,[])
#     for path in res:
#         print(*path,sep=' ')

# # 十八题
# def main():
#     prices = list(map(int,input().split()))
#     m = prices.pop()
#     specials = []
#     for _ in range(m):
#         sp = list(map(int,input().split()))
#         specials.append(sp)
#     needs = list(map(int,input().split()))
#     n = len(prices)
#     def dfs(cur_needs:tuple):
#         cur_needs = list(cur_needs)
#         cost = sum(cur_needs[i]*prices[i] for i in range(n))
#         for sp in specials:
#             new_needs = []
#             for i in range(n):
#                 if sp[i] > cur_needs[i]:
#                     break
#                 new_needs.append(cur_needs[i]-sp[i])
#             else:
#                 cost = min(cost, sp[-1]+dfs(tuple(new_needs)))
#         return cost
#     print(dfs(tuple(needs)))

# # 十九题
# def main():
#     nums = list(map(int,input().split()))
#     k = int(input())
#     total = sum(nums)
#     if total%k != 0:
#         print('false')
#         return 
#     target = total // k
#     nums.sort(reverse=True)
#     buckets = [0]*k
#     def backtrack(index)->bool:
#         if index == len(nums):
#             return all(b==target for b in buckets)
#         num = nums[index]
#         for i in range(k):
#             if buckets[i]+num <= target:
#                 buckets[i] = buckets[i]+num
#                 if backtrack(index+1):
#                     return True
#                 buckets[i] = buckets[i]-num
#             if buckets[i] == 0:
#                 break
#         return False
#     isOk = backtrack(0)
#     if isOk:
#         print('true')
#     else:
#         print('false')

# # 二十题
# def main():
#     nums = list(map(int,input().split()))
#     nums.sort(reverse=True)
#     for i in range(len(nums)):
#         if sum(nums[:i+1])==sum(nums[i+1:]):
#             print("true")
#             return 
#     print("false")
#     return

# # 二十一题
# def main():
#     n = int(input())
#     dp = [0]*(n+1)
#     dp[2] = 1
#     for i in range(3,n+1):
#         for j in range(1,i):
#             dp[i] = max(dp[i],j*(i-j),j*dp[i-j])
#     print(dp[n])

# # 二十二题
# def main():
#     nums = list(map(int,input().split()))
#     dp = [0]*(len(nums)+1)
#     dp[1] = nums[0]
#     for i in range(2,len(nums)+1):
#         dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
#     print(max(dp))

# # 二十三题
# def main():
#     nums = list(map(int,input().split()))
#     nums = [1] + nums + [1]
#     n = len(nums)
#     dp = [[0]*n for _ in range(n)]

#     for length in range(2,n):
#         for left in range(0, n-length):
#             right = left + length
#             for k in range(left+1,right):
#                 dp[left][right]=max(dp[left][right], 
#                                     dp[left][k]+nums[left]*nums[k]*nums[right]+dp[k][right] 
#                                     )
#     print(dp[0][n-1])

# # 二十四题
# def main():
#     n=int(input())
#     nums=list(map(int,input().split()))
#     res=[]
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if nums[i]+nums[j]+nums[k]==0:
#                     temp=[nums[i],nums[j],nums[k]]
#                     temp.sort()
#                     if temp not in res:
#                         res.append(temp)
#     res.sort()
#     print('[',end='')
#     for i in range(len(res)):
#         temp=res[i]
#         print('[',end='')
#         for j in range(3):
#             print(temp[j],end='')
#             if j!=2:
#                 print(',',end='')
#         print(']',end='')
#         if i!=len(res)-1:
#             print(',',end='')
#     print(']')

# # 二十五题
# def main():
#     s=list(input())
#     stack=[]
#     queue=[]
#     for i in range(len(s)):
#         if s[i]!=')':
#             stack.append(s[i])
#         else:
#             while True:
#                 temp=stack[-1]
#                 if temp!='(':
#                     queue.append(temp)
#                     stack.pop()
#                 else:
#                     stack.pop()
#                     for i in range(len(queue)):
#                         stack.append(queue[i])
#                     queue.clear()
#                     break
#     print("".join(stack))

# # 二十六题
# def main():
#     n = int(input())
#     nums = list(map(int,input().split()))
#     farthest = 0
#     end = 0
#     jump = 0
#     for i in range(n-1):
#         farthest = max(farthest, i+nums[i])
#         if i == end:
#             end = farthest
#             jump = jump+1
#     print(jump)

# # 二十七题
# def main():
#     n = int(input())
#     nums = list(map(int,input().split()))
#     num_dict = {0:0,1:0,2:0}
#     for i in nums:
#         num_dict[i]= num_dict[i]+1
#     new_nums = []
#     for i in range(num_dict[0]):
#         new_nums.append(0)
#     for i in range(num_dict[1]):
#         new_nums.append(1)
#     for i in range(num_dict[2]):
#         new_nums.append(2)
#     print("[" + ",".join(map(str, new_nums)) + "]")

# # 二十八题
# def main():
#     n = int(input())
#     a = list(map(int,input().split()))
#     w_max = 100000
#     w_i = -1
#     for i in range(n):
#         if a[i]< w_max:
#             w_max = a[i]
#             w_i = i
#     print(w_i+1)

# # 二十九题
# def main():
#     n = int(input())
#     nums = list(map(int,input().split()))
#     steps = 0
#     if n == 1:
#         print(0)
#     else:
#         for i in range(1,n):
#             if nums[i]>nums[i-1]:
#                 continue
#             else:
#                 steps = steps+nums[i-1]-nums[i]+1
#                 nums[i] = nums[i-1]+1
#         print(steps)

# # 三十题
# def main():
#     n,k=map(int,input().split())
#     res=[]
#     for i in range(21):
#         for j in range(35):
#             for h in range(0,301,3):
#                 if i*5+j*3+h/3==n and i+j+h==k:
#                     res.append([i,j,h])
#     if len(res)==0:
#         print(0)
#     else:
#         for i in range(len(res)):
#             print(*res[i])

# # 三十一题
# def main():
#     k,n = map(int,input().split())
#     res = []
#     def backtrack(start:int,path:list):
#         if sum(path)==n and len(path)==k:
#             res.append(path[:])
#             return
#         elif len(path)>=k or sum(path)>n:
#             return
#         for i in range(start,10):
#             path.append(i)
#             backtrack(i+1,path)
#             path.pop()
#     backtrack(1,[])
#     res.sort(reverse=True)
#     for r in res:
#         print(*r)
#     if not res:
#         print(0)

# # 三十二题
# def main():
#     import math
#     n = int(input())
#     if int(math.isqrt(n))**2 == n:
#         print(1)
#         return 
#     for i in range(1,int(math.isqrt(n))+1):
#         j = n - i*i
#         if int(math.isqrt(j))**2 == j:
#             print(2)
#             return
#     while n % 4 == 0:
#         n //= 4
#     if n % 8 == 7:
#         print(4)
#     else:
#         print(3)

# # 三十三题
# def main():
#     g = list(map(int,input().split()))
#     s = list(map(int,input().split()))
#     g.sort()
#     s.sort()
#     i=j=res = 0
#     while i < len(g) and j < len(s):
#         if g[i] <= s[j]:
#             res += 1
#             i += 1
#             j += 1
#         else:
#             j += 1
#     print(res)

# # 三十四题
# def main():
#     digits = input()
#     keyBorad = {
#         '2': 'abc',
#         '3': 'def',
#         '4': 'ghi',
#         '5': 'jkl',
#         '6': 'mno',
#         '7': 'pqrs',
#         '8': 'tuv',
#         '9': 'wxyz'
#     }
#     res = []
#     def backtrack(index, path):
#         if index == len(digits):
#             res.append(''.join(path))
#             return
#         possible_letters = keyBorad[digits[index]]
#         for letter in possible_letters:
#             path.append(letter)
#             backtrack(index + 1, path)
#             path.pop()
#     backtrack(0, [])
#     print('[' + ', '.join(res) + ']')

# # 三十五题
# def main():
#     n = int(input())
#     res = 0
#     used = [False]*(n+1)
#     def backtrack(i):
#         if i>n:
#             nonlocal res
#             res += 1
#             return
#         for x in range(1,n+1):
#             if not used[x] and (x % i == 0 or i % x == 0):
#                 used[x] = True
#                 backtrack(i+1)
#                 used[x] = False
#     backtrack(1)
#     print(res)

# # 三十六题
# def main():
#     n, c = map(int,input().split())
#     w_list = list(map(int, input().split()))
#     v_list = list(map(int, input().split()))
#     dp = [0]*(c+1)
#     for i in range(n):
#         w,v= w_list[i],v_list[i]
#         for j in range(c,w-1,-1):
#             dp[j]=max(dp[j],dp[j-w]+v)
#     print(max(dp))

# # 三十七题
# def main():
#     s = input()
#     n = len(s)
#     if n < 2:
#         return s
    
#     dp = [[False]*n for _ in range(n)]

#     start = 0
#     max_len = 1

#     for i in range(n):
#         dp[i][i] = True
    
#     for j in range(1,n):
#         for i in range(0,j):
#             if s[i] == s[j]:
#                 if j-i<3:
#                     dp[i][j]=True
#                 else:
#                     dp[i][j]=dp[i+1][j-1]
#             else:
#                 dp[i][j]=False

#             if dp[i][j] and (j-i+1)>max_len:
#                 start = i
#                 max_len = j-i+1
#     print(s[start:start+max_len])

# # 三十八题
# def sub_sum(nums,start,end):
#     res = 0
#     for i in range(start,end+1):
#         res = res + nums[i]
#     return res

# def main():
#     n = int(input())
#     nums = list(map(int,input().split()))
#     dp = [0]*n
#     dp[0] = nums[0]
#     for i in range(1,n):
#         max_sub_sum = 0
#         for j in range(i+1):
#             s_sum = sub_sum(nums,j,i)
#             if s_sum > max_sub_sum:
#                 max_sub_sum =s_sum
#         dp[i]=max_sub_sum
#     print(max(dp))











