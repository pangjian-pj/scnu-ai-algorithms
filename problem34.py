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
        if index == len(digits):
            res.append(''.join(path))
            return
        possible_letters = keyBorad[digits[index]]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    backtrack(0, [])
    print('[' + ', '.join(res) + ']')

if __name__ == '__main__':
    main()

