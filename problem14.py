# def main():
#     nums = list(map(int,input().split()))
#     l = len(nums)
#     res = []

#     # i是当前元素的下标，cur_xor是当前子集的异或和
#     def backtrack(i,cur_xor):
#         # 递归终止条件：对列表中的所有元素都遍历了一遍
#         if i==l:
#             res.append(cur_xor)
#             return
#         # 这是一个选/不选的回溯模型
#         # 不选元素i，则当前异或值不变
#         backtrack(i+1,cur_xor)
#         # 选了元素i，则当前需要做异或，异或的计算符号为^
#         backtrack(i+1,cur_xor^nums[i])

#     backtrack(0,0)
#     print(sum(res))

def main():
    nums = list(map(int, input().split()))
    n = len(nums)

    # 数学结论：所有子集的异或和等于所有元素按位或之后再乘以2^(n-1)
    or_val = 0
    for x in nums:
        # |是按位或运算符
        or_val =or_val|x 

    # <<左移运算符，左移一位表示乘以2，左移n-1位表示2^(n-1)
    print(or_val * (1 << (n - 1)))

if __name__ == "__main__":
    main()