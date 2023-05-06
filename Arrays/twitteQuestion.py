def my_func(n):
    result = []
    for i in range(n):
        result.append(lambda: i * 2)
    return result


func = my_func(3)
for f in func:
    print(f())
    break
