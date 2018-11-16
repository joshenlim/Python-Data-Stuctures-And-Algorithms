import math

def merge(inputArray, start, end):
    

def mergeSort(inputArray, start, end):
    if start < end:
        midpoint = math.floor(len(inputArray) / 2)
        mergeSort(inputArray, start, midpoint)
        mergeSort(inputArray, midpoint + 1, end)
        merge(inputArray, start, end)


data = [5, 3, 7, 2, 1, 8, 6, 4]

mergeSort(data, 0, len(data) - 1)
