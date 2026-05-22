def merge_sorted(a, b):
    result = []

    for i in range(len(a)):
        result.append(a[i])
    for i in range(len(b)):
        result.append(b[i])

    # сортировка пузырьком
    for _ in range(len(result)-1):
        for i in range(len(result)-1):
            if result[i+1] < result[i]:
                tmp = result[i]
                result[i] = result[i+1]
                result[i+1] = tmp
    return result

print(merge_sorted([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
print(merge_sorted([1, 2, 3], []))          # [1, 2, 3]