N = int(input())

x = 1
y = 1
move = input().split()

# L,R,U,D 구현
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for move in move:
    for i in range(len(move_type)):
        if(move == move_type[i]):
            nx = x + dx[i]
            ny = y + dy[i]
    if(nx < 1 or ny < 1 or nx > N or ny > N):
        continue
    x = nx
    y = ny

print(x, y)
