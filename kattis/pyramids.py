from math import sqrt

"""
LAYERS of a pyramid
Without using Math trick

To understand this problem, we should first understand how we get the total number of blocks from the number of layers. If we have 3 blocks, then Total = 1+2+3 = 6. Now, let's check the other way round.

Let say we now know the total number of bricks is 6, and we want to know the number of layers. We will keep decreasing the total until it is not negative.

CASE I.: Full layers
Total = 6 counter = 1 Total-1 = 6-1 = 5; counter = 2
Total-2 = 5-2 = 3; counter = 3
Total-3 = 3-3 = 0; counter = 4

STOP INCREMENTING counter when Total-counter < 0
Number_Layers = counter - 1 = 4-1 = 3

Case II. : Not every layers full

Total = 7 counter = 1 Total-1 = 7-1 = 6; counter = 2
Total-2 = 6-2 = 4; counter = 3
Total-3 = 4-3 = 1; counter = 4
Total-4 = 1-4 = -3< 0; counter = 5 STOP

STOP INCREMENTING counter when Total-counter < 0
Number_Layers = counter - 1 = 5-1 = 4



Using Math trick

given a function f(n), if f(n+1)-f(n) is a constant value r, then, the sum of
f(i) + f(i+1) + ... + f(k) = (k-i+1)*(f(k)+f(i))/2.
Particular Case: f(n) = n

==> f(n+1) = n+1

==> f(n+1) - f(n) = n+1-n = 1

==> f(1) + f(2) + ... + f(n) = 1 + 2 + ...+ n = n(n+1)/2

The sum S = n(n+1)/2 ==> n(n+1) = 2S

==> n^2 + n -2S = 0. This is a quadratic equation that can be easily solved in a close form

n1 = (-1-sqrt(1+8s))/2 n2 = (-1+sqrt(1+8s))/2

n1 <0 Not possible, hence, the solution is n2
"""
# blocks = int(input().strip())
blocks = 80
layerBlocks = 1
height = 0
while blocks > 0:
    blocks -= layerBlocks**2
    layerBlocks += 2
    height += 1
print(height - 1 if blocks < 0 else height)
