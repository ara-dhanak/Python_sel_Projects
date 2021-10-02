
def commonchar(str1,str2):
    ustr1 = list(set(str1))
    ustr2 = list(set(str2))
    max_length = len(ustr2)
    str1 = []
    str2 = []
    for i in range(len(ustr1)):
        if ustr1[i] in ustr2:
            continue
        else:
            str1.append(ustr1[i])
    for i in range((max_length)):
        if ustr2[i] in ustr1:
            continue
        else:
            str2.append(ustr2[i])
    print(str1)
    print(str2)
if __name__ == '__main__':
    str1 = 'cqarrt'
    str2 = 'betcarr'
    commonchar(str1,str2)