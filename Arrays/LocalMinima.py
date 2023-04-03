def localMinima(arr):
    n = len(arr)
    lst = []
    if n < 3:
        return -1
    for i in range(1, n - 1):
        if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
            lst.append(arr[i])
            lst = sorted(lst)

    if len(lst) < 1:
        return -1
    return lst[-1]


print(localMinima([40, 35, 50, 10, 35, 50]))
