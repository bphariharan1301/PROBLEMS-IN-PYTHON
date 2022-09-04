from collections import Counter


def repeatChar(string):
    count = Counter(string)
    for item in count:
        if count[item] > 1:
            print('{} occurs {}'.format(item, count[item]))


string = input()
repeatChar(string)
