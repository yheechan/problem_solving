N = int(input())
cycle_length = 0
std = N
while True:
  std_str = str(std)
  length = len(std_str)
  if length == 1:
    std_str += '0'
  next_num = int(std_str[0]) + int(std_str[1])
  new_num = str(std)[-1] + str(next_num)[-1]
  cycle_length += 1
  if int(new_num) == N:
    break
  std = new_num
print(cycle_length)
