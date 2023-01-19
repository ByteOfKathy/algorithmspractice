numBooks = int(input().strip())
numDiscounts = numBooks // 3
pay = []
group = []
total = 0
remove = 2
for i in range(numBooks):
    pay.append(int(input()))
pay.sort(reverse=True)
for i in range(numDiscounts):
    pay[remove] = 0
    remove += 3
for i in pay:
    total += i
print(total)