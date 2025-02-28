N, M = input().split()
N, M = int(N), int(M)
cards = [int(x) for x in input().split()]
diff_min = 300001
answer = 0
for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            card_sum = cards[i] + cards[j] + cards[k]
            diff = M - card_sum
            if diff < diff_min and diff >= 0:
                diff_min = diff
                answer = card_sum
print(answer)