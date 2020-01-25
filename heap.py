arr = [None,9,7,6,12,8,17] # unsorted
midpoint = 0

def heapify(arr):

    if len(arr) % 2 == 0: # even
        midpoint = len(arr)/2
    else: # odd
        midpoint = len(arr)/2 + 1

    rightchild = midpoint*2 + 1
    leftchild = midpoint*2
    
    myMax = arr[midpoint]
    bigger = midpoint

    if rightchild is not None:
        if arr[rightchild] > arr[leftchild]:
            myMax = arr[rightchild]
            bigger = rightchild
        elif arr[rightchild] < arr[leftchild]:
            myMax = arr[leftchild]
            bigger = leftchild

    arr[midpoint], arr[bigger] = arr[bigger], arr[midpoint]
