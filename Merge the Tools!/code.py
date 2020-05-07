def merge_the_tools(string, k):
    str_len = len(string)
    for t in range(0,str_len, k):
        u = string[t:t+k]
        print(''.join(sorted(set(u), key=u.index)))


