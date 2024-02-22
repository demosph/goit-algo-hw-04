import timeit
import random

# Алгоритм сортування вставками
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

numbers = [5, 3, 8, 4, 2]
insertion_sort(numbers)

# Функція для випадкового генерування масиву з заданою довжиною
def generate_random_array(length):
    return [random.randint(0, 1000) for _ in range(length)]

def main():
    array_sizes = [100, 1000, 5000, 10000]

    for size in array_sizes:
        array = generate_random_array(size)
        # Час виконання алгоритму сортування злиттям
        merge_sort_time = timeit.timeit(lambda: merge_sort(array.copy()), number=10)

        # Час виконання алгоритму сортування вставками
        insertion_sort_time = timeit.timeit(lambda: insertion_sort(array.copy()), number=10)

        # Час виконання Timsort (вбудований алгоритм сортування в Python)
        timsort_time = timeit.timeit(lambda: sorted(array.copy()), number=10)

        print(f"Array size: {size}")
        print(f"Merge Sort Time: {merge_sort_time}")
        print(f"Insertion Sort Time: {insertion_sort_time}")
        print(f"Timsort Time: {timsort_time}")
        print("\n")

if __name__ == "__main__":
    main()