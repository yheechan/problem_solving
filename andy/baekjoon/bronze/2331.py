x_str = input()
x = int(x_str)
baseline = x - len(x_str) * 9
found = 0
if baseline < 0: baseline = 0
for std in range(baseline, x+1):
  std_str = str(std)
  ind_nums = [int(y) for y in std_str]
  test = std + sum(ind_nums)
  if test == x:
    found = 1
    break
if found == 1:
  print(std_str)
else:
  print(0)