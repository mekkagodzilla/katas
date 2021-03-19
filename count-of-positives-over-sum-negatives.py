'''
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is 
the sum of negative numbers.

If the input array is empty or null, return an empty array.
'''
def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    countPositives = len([x for x in arr if x > 0])
    sumNegatives = sum([item for item in arr if item <0])
    return [countPositives, sumNegatives]
