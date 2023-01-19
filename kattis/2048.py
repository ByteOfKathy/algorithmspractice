class num:
    def __init__(self, n, c = False):
        if not isinstance(n, int):
            raise TypeError("param needs to be an integer")
        self.number = n
        if not isinstance(c, bool):
            raise TypeError("param needs to be a boolean")
        self.__combined = c

    def toggleCombined(self):
        self.__combined = not self.__combined
    
    def isCombined(self):
        return self.__combined

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return self.number

board = []
for i in range(4):
    board.append([num(int(i)) for i in input().strip().split()])
myKey = int(input())

if myKey == 0: # left
    for row in board:
        for i in range(3):
            if row[i+1].number == row[i].number and not row[i].isCombined():
                row[i] = num(row[i].number * 2)
                row[i].toggleCombined()
                row.remove(row[i+1])
                row.append(num(0))
            if row[i+1].number == 0:
                row.remove(row[i+1])
                row.append(num(0))
            if row[i].number == 0:
                row.remove(row[i])
                row.append(num(0))
# elif myKey == 1: # up

elif myKey == 2: # right
    for row in board:
        for i in range(3, 0, -1):
            if row[i].number == row[i-1].number and not row[i].isCombined():
                row[i-1] = num(row[i].number * 2)
                row[i-1].toggleCombined()
                if i == 3:
                    row[i] = num(0)
                else:
                    row.remove(row[i])
                    row.append(num(0))
            if row[i-1].number == 0:
                row[i-1] = row[i]
                row[i] = num(0)
# else: # down

for row in board:
    for i in range(4):
        row[i] = str(row[i])
    print(' '.join(row))