from collections import deque


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


# 직접적으로 queue에 하나의 값을 더 추가하는 건 메모리상 무리가 갈 수 있음
# 가급적 이미 제공된 형태들을 활용하여 문제를 풀어보자
def shortest_distance(maps):
    n, m = len(maps[0]), len(maps)
    visited = [[False] * n for _ in maps]

    q = deque()
    q.append([0, 0])

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if (0 <= next_x < n) and (0 <= next_y < m):
                if maps[next_y][next_x] and not visited[next_y][next_x]:
                    visited[next_y][next_x] = True
                    q.append([next_x, next_y])
                    maps[next_y][next_x] = maps[cur_y][cur_x] + 1

    if maps[m-1][n-1] == 1:
        return -1

    return maps[m-1][n-1]


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(shortest_distance(maps))
