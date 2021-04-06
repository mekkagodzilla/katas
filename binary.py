def binary_array_to_number(arr):
    binstring = ''
    for digit in arr:
        binstring = binstring + str(digit)
    return int(binstring, 2)


print(binary_array_to_number([0, 0, 0, 1]))
print(binary_array_to_number([0, 0, 1, 0]))
print(binary_array_to_number([1, 1, 1, 1]))
print(binary_array_to_number([0, 1, 1, 0]))
