def find_duplicates(lst):
    if not lst:
        return []
    lst_sorted = sorted(lst)
    duplicates = []
    for i in range(len(lst_sorted) - 1):
        if lst_sorted[i] == lst_sorted[i + 1]:
            # если ещё не добавляли этот дубликат
            if lst_sorted[i] not in duplicates:
                duplicates.append(lst_sorted[i])
    return duplicates

print(find_duplicates([1, 2, 3, 1, 4, 2, 5]))  # [1, 2]
print(find_duplicates([1, 1, 1, 1]))            # [1]
print(find_duplicates([1, 2, 3, 4]))            # []
print(find_duplicates([]))                      # []