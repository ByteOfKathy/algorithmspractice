# s is heap size
# i is root of subtree
def heapify(arr, s,  i):
    # assume largest right now is root
    largest = i
    l = i * 2 + 1 # left child
    r = i * 2 + 2 # right child

    # check if left child exists and is greater than root
    if l < s and arr[i] < arr[l]:
        largest = l
    
    # check if right child exists and is greater than largest aka current root
    if r < s and arr[largest] < arr[r]:
        largest = r

    # make the swap if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Heapify swapped root
        heapify(arr, s, largest)
    
def maxheapsort(arr):
    # size of arr
    s = len(arr)

    for i in range(s, -1, -1):
        heapify(arr, s, i)
    
    # element extraction one by one
    for i in range(s-1, 0, -1): 
        # swap 
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0) 

# main

arr = [ 12, 11, 13, 5, 6, 7] 
maxheapsort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 