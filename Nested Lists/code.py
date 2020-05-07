from collections import Counter
if __name__ == '__main__':
    dict = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dict[name] = score
    
    fetch = sorted(Counter(dict.values()).items())
    # print(fetch[1][0])

    dict = sorted(dict.items(), key = lambda kv:(kv[1], kv[0]))
    for key, value in dict: 
         if value == fetch[1][0]: 
             print(key)

