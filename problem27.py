'''
    description: 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
    method: 这道题有多种写法，最简单的就是直接用sort，难一点的就是用指针，但这里提供一个思路，可以先算出0，1，2各有多少个元素，然后再依次打印出来。但是这道题最坑的地方在于这个输出格式，如果直接用python打印列表的方式，元素之间是默认带逗号与空格的，而题目要求不带空格。
'''
def main():
    n = int(input())
    nums = list(map(int,input().split()))
    num_dict = {0:0,1:0,2:0}
    for i in nums:
        num_dict[i]= num_dict[i]+1
    new_nums = []
    for i in range(num_dict[0]):
        new_nums.append(0)
    for i in range(num_dict[1]):
        new_nums.append(1)
    for i in range(num_dict[2]):
        new_nums.append(2)
    print("[" + ",".join(map(str, new_nums)) + "]")


if __name__ == '__main__':
    main()