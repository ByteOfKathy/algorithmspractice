myFile = open('test.in', 'r')
arr =  [int(i) for i in myFile.readline().strip().split()] # unsorted
arr.insert(0, None)
# print(arr)
midpoint = 0

def heapify(arr, elem):

    swapped = False 

    if len(arr) % 2 == 0: # even
        midpoint = len(arr)/2
    else: # odd
        midpoint = len(arr)/2 + 1

    rightchild = midpoint*2 + 1
    leftchild = midpoint*2
    
    # default is root
    myMax = arr[midpoint]
    bigger = midpoint

    if rightchild is not None:
        if arr[rightchild] > arr[leftchild]: # if right child is bigger
            myMax = arr[rightchild]
            bigger = rightchild
        elif arr[rightchild] < arr[leftchild]: # if left child is bigger
            myMax = arr[leftchild]
            bigger = leftchild

    arr[midpoint], arr[bigger] = arr[bigger], arr[midpoint] # swap
