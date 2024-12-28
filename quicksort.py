def quicksort(array):
    if len(array) < 2:
        return array 
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def main():
    print(quicksort([10, 5, 2, 3]))


if __name__ == "__main__":
    main()