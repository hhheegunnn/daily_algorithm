# 택시비 적게내기 - 미완성

from collections import deque


def visitable(N, x, y, board):
    return 0 <= x < N and 0 <= y < N and board[y][x] == 0


def solution(board):

    N = len(board)
    X, Y, DIRECTION, SUM = 0, 1, 2, 3
    UP, DOWN, RIGHT, LEFT = 0, 1, 2, 3
    DELTAS = [(-1, 0, LEFT), (1, 0, RIGHT), (0, 1, DOWN), (0, -1, UP)]
    que = deque([])

    if board[1][0] == 0:  # 아래
        que.append((0, 1, DOWN, 100))
    if board[0][1] == 0:  # 오른쪽
        que.append((1, 0, RIGHT, 100))
    board[0][0], board[1][0], board[0][1] = 1, 1, 1
    cand = []
    while que:
        cur = que.popleft()
        print(cur)
        if cur[X] == N-1 and cur[Y] == N-1:
            cand.append(cur[SUM])

        for dx, dy, d in DELTAS:
            if cur[DIRECTION] == d:
                next_p = (cur[X] + dx, cur[Y] + dy, d, cur[SUM] + 100)
            else:
                next_p = (cur[X] + dx, cur[Y] + dy, d, cur[SUM] + 500)
            print('>>', next_p)
            if visitable(N, next_p[X], next_p[Y], board) and board[next_p[Y]][next_p[X]] != 1:
                que.append(next_p)
                board[next_p[Y]][next_p[X]] = 1
            print(que)

    return cand
