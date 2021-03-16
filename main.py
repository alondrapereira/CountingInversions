def sort_and_count(arr):
    n = len(arr)
    count = 0
    if n > 1:
        midpoint = n // 2
        left_side = arr[:midpoint]
        right_side = arr[midpoint:]

        count += sort_and_count(left_side)
        count += sort_and_count(right_side)

        i = j = k = 0
        while i < len(left_side) and j < len(right_side):
            if left_side[i] <= right_side[j]:
                arr[k] = left_side[i]
                i += 1
            else:
                arr[k] = right_side[j]
                j += 1
                count += (len(left_side) - i)
            k += 1
        while i < len(left_side):
            arr[k] = left_side[i]
            i += 1
            k += 1
        while j < len(right_side):
            arr[k] = right_side[j]
            j += 1
            k += 1
    return count


if __name__ == '__main__':
    array = [1, 5, 3, -2, 2, 6, 90, 4, 8, 9, -3, 12]
    print("Before:")
    for i in array:
        print(i)
    inversions = sort_and_count(array)
    print("After:")
    for i in array:
        print(i)
    print("This array had %s inversions." % inversions)

