
def dp(items, N, K):
  max_value = -1

    



  return -1




def main():
  N, K = map(int, input().split())
  items = []
  for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

  res = dp(items, N, K)
  print(res)

if __name__ == "__main__":
  main()

