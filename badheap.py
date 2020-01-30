def heapify(arr):

    for i in range(len(arr)//2, 0, -1):
        swapped = True
        j = i

        if len(arr) % 2 == 0: # even
            midpoint = len(arr)//2
        else: # odd
            midpoint = len(arr)//2 + 1

        rightchild = midpoint*2 + 1
        leftchild = midpoint*2
        
        # default is root
        myMax = arr[midpoint]

        while leftchild < len(arr) and swapped : # making sure we aren't a leaf and a swap was performed or its the first iteration

            if(rightchild is None or rightchild >= len(arr)): # no right child
                # left child is smaller
                if arr[leftchild] < arr[j]:
                    arr[leftchild], arr[j] = arr[j], arr[leftchild]
                else:
                    swapped = False
            else: # right child exists
                if(arr[rightchild] < arr[leftchild]): # if right child is smaller
                    if(arr[rightchild] < arr[midpoint]): # if right child is smaller than parent, swap them
                        arr[rightchild], arr[midpoint] = arr[midpoint], arr[rightchild]
                    else:
                        swapped = False
                else: # if left child is smaller than right child
                    if(arr[leftchild] < arr[midpoint] ): # left child (smaller child) is smaller than parent, swap parent and child
                        arr[leftchild], arr[midpoint] = arr[midpoint], arr[leftchild]
                    else:
                        swapped = False

        return arr

        # if rightchild is not None:
        #     if arr[rightchild] > arr[leftchild]: # if right child is bigger
        #         myMax = arr[rightchild]
        #         bigger = rightchild
        #     elif arr[rightchild] < arr[leftchild]: # if left child is bigger
        #         myMax = arr[leftchild]
        #         bigger = leftchild
        


        # arr[midpoint], arr[bigger] = arr[bigger], arr[midpoint] # swap


myFile = open('test.in', 'r')
arr =  [int(i) for i in myFile.readline().strip().split()] # unsorted
arr.insert(0, None)
# print(arr)
midpoint = 0
print(heapify(arr))

