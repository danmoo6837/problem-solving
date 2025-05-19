from sys import stdin, stdout
from collections import deque

input = stdin.readline
queue = deque()

if __name__ == "__main__":
    n = int(input())
    visited = [False]*(n+1)
    arr = [[] for _ in range(n+1)]
    for i in range(n-1):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    result = [0]*(n+1)

    for i in arr[1]:
        queue.append(i)
        result[i] = 1
        visited[i] = True

    while queue:
        cur = queue.popleft()
        for j in arr[cur]:
            if visited[j] == False:
                queue.append(j)
                result[j] = cur
                visited[j] = True
    
    stdout.write('\n'.join(map(str, result[2:])))
