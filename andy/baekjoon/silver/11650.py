N = int(input())

coord = [list(map(int, input().split())) for i in range(N)]
sorted_coord = sorted(coord, key=lambda x: [x[0], x[1]])

for x, y in sorted_coord:
    print(x, y)
