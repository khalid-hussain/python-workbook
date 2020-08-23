def isSublist(larger: list, smaller: list) -> bool:
    if smaller[0] in larger:
        f_index = larger.index(smaller[0])
        sizeSmaller = len(smaller)
        subList = []

        for i in range(f_index, f_index + sizeSmaller):
            subList.append(larger[i])

        if subList == smaller:
            return True
        else:
            return False
    else:
        return False


def main():
    listA = [1, 2, 3, 4]
    listB = [-2, -1, 0, 1, 2, 3, 4]
    listC = [1, 2, 3, 4, 5, 6, 7, 8]

    print('Case 1:', isSublist(listB, listA))
    print('Case 2:', isSublist(listC, listA))


if __name__ == "__main__":
    main()
