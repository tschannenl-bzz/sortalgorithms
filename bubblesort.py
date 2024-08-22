
def Bubblesort(array: list, sort_option: int):
    """

    Sort Options:
    (1) Nachname
    (2) PLZ
    (3) Geburtsdatum (dd.mm.yyyy)
    (4) Vermögen (Decimal)
    """

    options = [2, 4, 5, 6]  # CSV Header Positions of the Options
    option = options[sort_option - 1]

    n = len(array)

    def swap(x: int, y: int):
        _x, _y = array[x], array[y]
        array[y] = _x
        array[x] = _y

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if array[j][option] > array[j + 1][option]:
                swap(j, j + 1)
                swapped = True

        if not swapped:
            return
