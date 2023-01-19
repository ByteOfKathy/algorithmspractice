from queue import FIFOqueue

fifo = FIFOqueue(1)

def test_enqueue():
    fifo.enqueue(9)
    expected = [1, 9]
    for i in expected:
        assert fifo.arr[i] == expected

def test_dequeue():
    fifo.dequeue()
    expected = [9]
    for i in expected:
        assert fifo.arr[i] == expected
    
print("Tests passed YAY")