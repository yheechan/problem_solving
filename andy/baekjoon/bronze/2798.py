N, M = map(int, input().split()) # unpacking
c_list = sorted(list(map(int, input().split())), reverse=True)

sum = 0
for i in range(N):
    f_n = c_list[i]
    for j in range(i+1, N):
        s_n = c_list[j]
        for k in range(j+1, N):
            temp = f_n + s_n + c_list[k]
            if temp > sum and  temp <= M:
                sum = temp

print(sum)
