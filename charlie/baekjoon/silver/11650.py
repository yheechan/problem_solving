N = int(input())
coordinates = [list(map(int, input().split())) for _ in range(N)]

sorted_coord = sorted(coordinates, key=lambda x: (x[0], x[1]))

for x, y in sorted_coord:
  print(x, y)
