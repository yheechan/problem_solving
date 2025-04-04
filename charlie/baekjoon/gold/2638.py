






import sys

class Grid:
    def __init__(self, ):
        pass


class Paper:
    def __init__(self, ):
        self.cheeze
        pass




def main():
    # N: vertical 세로
    # M: horizontal 가로
    input = sys.stdin.read
    data = input().split("\n")
    N, M = map(int, data[0].strip().split())

    P = Paper()

    paper = []
    for i in range(1, N+1):
        row = list(map(int, data[i].split()))
        paper.append(row)

if __name__ == "__main__":
    main()

