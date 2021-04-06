'''
You have a list of integers. The task is to return the maximum sum of the elements
located between two negative elements, or -1 if there are no such things.
No negative element should be present in this sum.

Example
[4, -1, 6, -2, 3, 5, -7, 7] -> 8

'''


def max_sum_between_two_negatives(arr):
    candidates = []
    negativeNumIndeces = []
    for i in range(len(arr)):
        if arr[i] < 0:
            negativeNumIndeces.append(i)

    for i in range(len(negativeNumIndeces) - 1):
        sumToAppend = sum(arr[negativeNumIndeces[i] + 1 : negativeNumIndeces[i+1]])
        candidates.append(sumToAppend)

    if candidates:
        return max(candidates)
    return -1

a = [4, -1, 6, -2, 3, 5, -7, 7]
b = max_sum_between_two_negatives(a)
print(b)