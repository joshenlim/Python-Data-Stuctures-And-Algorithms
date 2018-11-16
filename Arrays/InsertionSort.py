def insertionSort(inputArray):
    size = len(inputArray)

    for i in range(0, size):
        for j in range(i, 0, -1):
            if inputArray[j] < inputArray[j-1]:
                inputArray[j], inputArray[j-1] = inputArray[j-1], inputArray[j]
            else:
                 break;

    return inputArray

data = [5, 3, 7, 2, 1, 8, 6, 4, 2, 0]

sortedArray = insertionSort(data)
print(sortedArray)
