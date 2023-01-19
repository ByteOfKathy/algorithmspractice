import heap

# main

myfile = open("heap.in", "r")
arr = [int(i) for i in myfile.readline().strip().split()]
heap.maxheapsort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i]),

print(arr)
myfile.close()
