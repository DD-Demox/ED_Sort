def quick_sort(list_to_sort, start=0, end=None):
    if end is None:
        end = len(list_to_sort)
    if start < end:
        pivot = partition(list_to_sort, start, end)
        quick_sort(list_to_sort, start, pivot)
        quick_sort(list_to_sort, pivot + 1, end)
    return list_to_sort


def partition(list_to_sort, start, end):
    pivot = list_to_sort[end - 1]

    for i in range(start, end):
        if list_to_sort[i] <= pivot:
            list_to_sort[i], list_to_sort[start] = list_to_sort[start], list_to_sort[i]
            start += 1

    return start - 1


if __name__ == '__main__':

    a = [8, 5, 12, 55, 3, 7, 82, 44, 35, 25, 41, 29, 17]
    print(a)
    print(quick_sort(a))
    print(a)