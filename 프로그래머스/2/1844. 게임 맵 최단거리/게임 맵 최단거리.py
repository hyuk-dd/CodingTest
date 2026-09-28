from collections import deque

def solution(maps):
    # 좌, 우, 상, 하 입력 버튼 생성
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    todo = deque()
    start = [0, 0, 1]
    todo.append(start)
    visited[0][0] = True

    while todo:
        x, y, move = todo.popleft()
        
        # 도착지에 도달하면 중단
        if x == n-1 and y == m-1:
            return move
        
        # 상하좌우 이동 가능 좌표 체크
        for i in range(4):
            check_x = x + dx[i]
            check_y = y + dy[i]

            # 맵의 크기를 넘어가는 순간 제외
            if check_x < 0 or check_x >= n or check_y < 0 or check_y >= m:
                continue
            
            # 방문한 곳이면 제외
            if visited[check_x][check_y]:
                continue
            
            # 벽을 만났으면 제외
            if maps[check_x][check_y] == 0:
                continue

            todo.append([check_x, check_y, move+1])    # 여기서 추가되는 것은 [행, 열]임!
            visited[check_x][check_y] = True

    return -1