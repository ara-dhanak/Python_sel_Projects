def substring(input_string):
    length = len(input_string)
    emptyl = []

    for p in range(0,length):
        for q in range(p,length):
            emptyl.append(input_string[p:(q+1)])

    for i in emptyl:
        print(i)


if __name__ == '__main__':
    #inputstr = input()
    inputstr = 'abcd'
    substring(inputstr)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
