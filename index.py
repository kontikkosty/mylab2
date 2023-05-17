def binary_array_to_number(arr):
    binary_string = ''.join(str(bit) for bit in arr)
    decimal_number = int(binary_string, 2)
    return decimal_number
