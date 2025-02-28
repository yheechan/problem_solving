x = input()
origin = int(x)
count = 0

while True:
    count += 1
    right_origin_num = x[-1]
    right_sum_num = str(sum([int(y) for y in x]))[-1]
    x = right_origin_num + right_sum_num
    if origin == int(x):
        print(count)
        break

    



