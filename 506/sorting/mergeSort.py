from typing import List


def mergeSort(lst: List[int]) -> List[int]:
    pass

  
'''
merge sort alg
https://www.scaler.com/topics/merge-sort-in-python/
'''
  
  
  
'''
merge two sorted array
'''
def mergeTwoSorted(lst1, lst2):
    l = []
    i1, i2 = 0, 0
    while i1 < len(lst1) and i2 < len(lst2):
        l.append(min(lst1[i1], lst2[i2]))
        if lst1[i1] >= lst2[i2]:
            i2 += 1
        else:
            i1 += 1
    while i1 < len(lst1):
        l.append(lst1[i1])
        i1+=1
    while i2 < len(lst2):
        l.append(lst2[i2])
        i2+=1
    return l

if __name__ == '__main__':
    list1 = [1, 2]
    list2 = [3, 4]

    result = mergeTwoSorted(list1, list2)
    for i in result:
        print(i, end=", ")

