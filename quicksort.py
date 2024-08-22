
def Quicksort(array: list, sort_option: int):
    """

    Sort Options:
    (1) Nachname
    (2) PLZ
    (3) Geburtsdatum (dd.mm.yyyy)
    (4) Vermögen (Decimal)
    """

    options = [2, 4, 5, 6]  # CSV Header Positions of the Options
    option = options[sort_option - 1]
    
    def partition(arr, low, high):
        pivot = arr[high][option]
        i = low - 1
        for j in range(low, high):
            if arr[j][option] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort_for_second_entry(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quicksort_for_second_entry(arr, low, pi - 1)
            quicksort_for_second_entry(arr, pi + 1, high)


    quicksort_for_second_entry(array, 0, len(array) - 1)
