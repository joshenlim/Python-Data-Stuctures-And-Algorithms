def mergeSort(inputArray):
    if (len(inputArray) > 1):
        mid = len(inputArray) // 2
        leftHalf = inputArray[:mid]
        rightHalf = inputArray[mid:]
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        merge(inputArray, leftHalf, rightHalf)

def merge(inputArray, leftHalf, rightHalf):
    i = 0
    j = 0
    k = 0

    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] < rightHalf[j]:
            inputArray[k] = leftHalf[i]
            i = i + 1
        else:
            inputArray[k] = rightHalf[j]
            j = j + 1
        k = k + 1

    # when rightHalf is empty
    while i < len(leftHalf):
        inputArray[k] = leftHalf[i]
        i = i + 1
        k = k + 1

    # when leftHalf is empty
    while j < len(rightHalf):
        inputArray[k] = rightHalf[j]
        j = j + 1
        k = k + 1

data = [5, 3, 7, 2, 1, 8, 6, 4, 5]
mergeSort(data)
print(data)
