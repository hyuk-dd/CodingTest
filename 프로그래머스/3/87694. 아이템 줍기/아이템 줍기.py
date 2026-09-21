from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표 최대값이 50이므로, 2배로 늘린 100보다 넉넉하게 102로 설정
    MAX = 102 
    board = [[-1] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]
    
    # 1. 모든 직사각형의 좌표를 2배로 확장하여 맵에 그리기
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # 직사각형 내부는 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 0
                # 테두리인 경우, 다른 직사각형의 내부(0)가 아닌 경우에만 1로 채움
                elif board[i][j] != 0:
                    board[i][j] = 1
                    
    # 2. 시작점 및 목표점 좌표도 2배로 확장
    cx, cy = characterX * 2, characterY * 2
    ix, iy = itemX * 2, itemY * 2
    
    # 3. BFS 탐색 시작
    q = deque([(cx, cy, 0)]) # (x, y, 이동 거리)
    visited[cx][cy] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y, dist = q.popleft()
        
        # 목표 지점에 도달하면, 늘려놨던 거리를 다시 2로 나누어 반환
        if x == ix and y == iy:
            return dist // 2
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵 범위 내에 있고, 테두리(1)이면서, 아직 방문하지 않은 곳으로만 이동
            if 0 <= nx < MAX and 0 <= ny < MAX:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))
                    
    return 0