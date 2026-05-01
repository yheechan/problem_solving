# initialize map size
n, m = map(int, input().split())

# coverage map
d = [[0] * m for _ in range(n)]

# current position and direction
x, y, direction = map(int, input().split())
d[x][y] = 1


array = []
for i in range(n):
  array.append(list(map(int, input().split())))

# N, E, S, W
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# turn left
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3
  print("turn left")

# start simulation
count = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]

  if d[nx][ny] == 0 and array[nx][ny] == 0:
    print("I can go, not ocean or covered")
    print(f"Mark ({nx}, {ny}) covered")
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else:
    print("I can't go")
    turn_time += 1

  if turn_time == 4:
    print("Go backward, for I have turned all four direction")
    nx = x - dx[direction]
    ny = y - dy[direction]

    if array[nx][ny] == 0:
      print(f"I can go, backward, ({nx}, {ny})")
      x = nx
      y = ny
    else:
      print(f"I can't go backward {count}")
      break
    turn_time = 0

print(count)
