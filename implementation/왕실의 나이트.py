input = input()
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
x = dict[input[0]]
y = int(input[1])
count = 0
#UL, UR, RU, RD, DL, DR, LU, LD
dx = [-1, 1, 2, 2, -1, 1, -2, -2]
dy = [-2, -2, -1, 1, 2, 2, -1, 1]

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if(nx < 1 or ny < 1 or nx > 8 or ny > 8):
        continue
    count += 1

print(count)
