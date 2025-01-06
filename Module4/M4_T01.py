from heapq import merge


def merge_sort(collection):
    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    left = merge_sort(collection[:mid])
    right = merge_sort(collection[mid:])
    return merge(left, right)


print(*merge_sort([1, 3, 2, 4, 5, 6, 7, 8, 9, 0]))