T = int(input())

test = []
max_n = -1
for i in range(T):
  k = int(input())
  n = int(input())
  if n > max_n:
      max_n = n
  test.append((k, n))

room_data = [[0] * 15 for _ in range(15)]
for i in range(max_n):
    room_data[0][i] = i+1


for floor in range(1, 15):
  for room in range(max_n):
    for r in range(room+1):
      room_data[floor][room] += room_data[floor-1][r]


for k, n in test:
  print(room_data[k][n-1])


