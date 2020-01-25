arr = [None,9,7,6,12,8,17] # unsorted
midpoint = 0

def heapify(arr):

    if len(arr) % 2 == 0: # even
        midpoint = len(arr)/2
    else: # odd
        midpoint = len(arr)/2 + 1

