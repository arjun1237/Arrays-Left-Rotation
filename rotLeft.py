def rotLeft(a, d):
    array_len = len(a)
    d = d % array_len
    new_arr = [None] * array_len
    count = 0

    for i in range(d, array_len):
        new_arr[count] = a[i]
        count += 1
    for i in range(0, d):
        new_arr[count] = a[i]
        count += 1

    return new_arr