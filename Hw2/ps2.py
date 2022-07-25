# -*- coding: UTF-8 -*-

from os import remove


def Permutation(str):
    '''
    input: a string
    output: a list of permutations of this str
    noting: if the str contains repeated letters, the result will include duplicates
    '''
    ls = list(str)
    # 只有一个字母时，返回自身
    if len(ls) == 1:
        return [str]
    else:
        output = []
        for e in ls:    # 每次固定第一个字母
            removedLs = ls[:]
            removedLs.remove(e)
            for perm in Permutation(''.join(removedLs)):
                # 否则，每次固定第一个字母，在后面加上剩下字母的排列
                output.append(''.join([e]+list(perm)))
        return output


# # TEST
# # str = 'abb'
# str = 'abcde'
# print (Permutation(str))
# print(len(Permutation(str)))

if __name__ == '__main__':
    str = input("Please enter a string: ")
    perms = set(Permutation(str))
    print("The permutations of the string you entered is: ")
    for p in perms:
        print(p)
