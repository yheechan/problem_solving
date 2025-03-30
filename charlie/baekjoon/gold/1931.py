def greedy(meetings):
  curr = (-1, -1)
  sack = []

  for m in meetings:
    c_s, c_e = curr
    p_s, p_e = m

    if p_s >= c_e:
      sack.append(m)
      curr = m

  return sack

def main():
  N = int(input())
  meetings = []
  for _ in range(N):
    s, e = map(int, input().split())
    meetings.append((s, e))

  meetings = sorted(meetings, key=lambda x: (x[1], x[0]))
  
  res = greedy(meetings)
  print(len(res))

if __name__ == "__main__":
  main()

