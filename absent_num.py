# Python program to print all
# sublist from a given list

# function to generate all the sub lists
def sub_lists(l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists
# Function to find the missing element


def getMissingNo(arr, n):
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(arr)
    return total - sum_of_A


# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 5]
    N = len(arr)

    # Function call
    miss = getMissingNo(arr, N)
    print(miss)

# This code is contributed by Pratik Chhajer

# driver code
l1 = [1, 2, 3]
print(sub_lists(l1))

'''

'''
