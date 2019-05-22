arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def getCombinations(arr):
    if(len(arr) == 1):
        return [arr]
    subs = getCombinations(arr[1:])
    newers = [x+[arr[0]] for x in subs]
    return subs + newers + [[arr[0]]]


print(getCombinations(arr))
print(len(getCombinations(arr)))