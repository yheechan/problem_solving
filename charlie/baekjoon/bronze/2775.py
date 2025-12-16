T = int(input())

room_data = [[0] * 15 for _ in range(15)]


test = []
for i in range(T):
    k = int(input())
    n = int(input())
    test.append((k, n))

for k, n in test:
    # fill 0th floor
    if k == 1:
        for i in range(n):
            room_data[k-1][i] = i+1

    # fill current floor
    for room in range(n):
        for below_room in range(room+1):
            if room_data[k-1][below_room] == 0:
                # fill this room first
                for r in range(below_room+1):
                    room_data[k-1][below_room] += room_data[k-2][r]
                    
            room_data[k][room] += room_data[k-1][below_room]

    print(room_data[k][n-1])

