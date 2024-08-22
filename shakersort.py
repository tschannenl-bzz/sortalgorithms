
def Shakersort(array: list, sort_option: int):
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

    swapped = True
    start = 0
    end = n-1
    while (swapped==True):
        swapped = False
 
        for i in range (start, end):
            if (array[i][option] > array[i+1][option]) :
                swap(i, i+1)
                swapped=True

        if (swapped==False):
            break
 
        swapped = False

        end = end-1
 
        for i in range(end-1, start-1,-1):
            if (array[i][option] > array[i+1][option]):
                swap(i, i+1)
                swapped = True
 
        start = start+1
