def network(n, computers):
    visited = [False] * n
    count = 0

    def dfs(cur):
        visited[cur] = True

        for idx in range(n):
            if not visited[idx] and computers[cur][idx]:
                dfs(idx)

    for node_idx in range(n):
        if not visited[node_idx]:
            dfs(node_idx)
            count += 1

    return count

