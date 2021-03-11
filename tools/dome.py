def bubble_sort(data, key):

    length = len(data)
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if (data[j][key] < data[j + 1][key]):
                tmp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = tmp
