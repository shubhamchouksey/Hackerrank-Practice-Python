def swap_case(s):
    lst = []
    for c in s:
        if ord(c) in range(65,92):
            lst.append(chr(ord(c)+32))
        elif ord(c) in range(97,123):
            lst.append(chr(ord(c)-32))
        else:
            lst.append(chr(ord(c)))

    return ''.join(str(i) for i in lst)


