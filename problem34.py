def main():
    digits = input()
    keyBorad = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    res = []
    def backtrack(index, path):
        # 递归终止条件：遍历完所有的数字
        if index == len(digits):
            res.append(''.join(path))
            return
        # 这里是数字对应的字母给取出来
        possible_letters = keyBorad[digits[index]]
        for letter in possible_letters:
            # 这里就是回溯的经典三步法，先取，然后递归下一个，再吐出来
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    backtrack(0, [])
    print('[' + ', '.join(res) + ']')

if __name__ == '__main__':
    main()

