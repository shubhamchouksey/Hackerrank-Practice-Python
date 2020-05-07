from collections import Counter
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unq_arr = Counter(arr).keys()
    print(sorted(unq_arr)[-2])

