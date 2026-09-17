def dfs(board, x, y, target, visited, n):
    """
    주어진 보드에서 상하좌우로 연결된 특정 값(target)의 좌표들을 찾아 반환하는 DFS 함수입니다.
    - target = 0 : game_board에서 빈 공간을 찾을 때 사용
    - target = 1 : table에서 퍼즐 조각을 찾을 때 사용
    """
    # 이동할 방향 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # DFS를 위한 스택 초기화 및 시작점 방문 처리
    stack = [(x, y)]
    visited[x][y] = True
    block = [(x, y)] # 찾아낸 좌표들을 담을 리스트
    
    while stack:
        cx, cy = stack.pop()
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            
            # 보드 범위를 벗어나지 않고, 아직 방문하지 않았으며, 찾는 값(target)과 일치한다면
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and board[nx][ny] == target:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                    block.append((nx, ny))
                    
    return block

def normalize(block):
    """
    추출한 블록의 좌표를 (0, 0) 기준으로 맞추어 정규화하는 함수입니다.
    보드 내의 절대 좌표가 달라도, 모양이 같으면 동일한 블록으로 취급하기 위함입니다.
    """
    # 블록 내 가장 작은 x좌표와 y좌표를 찾음
    min_x = min(b[0] for b in block)
    min_y = min(b[1] for b in block)
    
    # 모든 좌표에서 최솟값을 빼주어 좌상단을 (0,0)으로 당기고 정렬하여 반환
    return sorted([(b[0] - min_x, b[1] - min_y) for b in block])

def rotate(block):
    """
    블록을 시계 방향으로 90도 회전시키는 함수입니다.
    (x, y)를 시계방향으로 90도 회전하면 (y, -x)가 됩니다.
    """
    rotated = [(b[1], -b[0]) for b in block]
    return normalize(rotated) # 회전 후 음수 좌표가 생길 수 있으므로 다시 정규화

def solution(game_board, table):
    n = len(game_board)
    empty_spaces = [] # 게임 보드의 빈 공간들
    puzzles = []      # 테이블의 퍼즐 조각들
    
    visited_board = [[False] * n for _ in range(n)]
    visited_table = [[False] * n for _ in range(n)]
    
    # 1. game_board에서 빈 공간(0) 덩어리들을 추출
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and not visited_board[i][j]:
                block = dfs(game_board, i, j, 0, visited_board, n)
                empty_spaces.append(normalize(block))
                
    # 2. table에서 퍼즐 조각(1) 덩어리들을 추출
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not visited_table[i][j]:
                block = dfs(table, i, j, 1, visited_table, n)
                puzzles.append(normalize(block))
                
    answer = 0
    used_puzzles = [False] * len(puzzles) # 사용한 퍼즐 조각 체크용 배열
    
    # 3. 추출한 빈 공간에 퍼즐 조각을 하나씩 맞춰보기
    for space in empty_spaces:
        matched = False # 현재 빈 공간이 채워졌는지 여부
        
        for i, puzzle in enumerate(puzzles):
            if used_puzzles[i]: # 이미 사용된 조각이면 패스
                continue
            
            if len(space) != len(puzzle): # 칸 수가 다르면 애초에 맞을 수 없으므로 패스
                continue
                
            rotated_puzzle = puzzle
            
            # 4방향으로 회전시키며 빈 공간과 모양이 완전히 일치하는지 확인
            for _ in range(4):
                if space == rotated_puzzle: # 모양이 일치하면
                    used_puzzles[i] = True  # 퍼즐을 사용 처리
                    answer += len(space)    # 채운 칸 수만큼 정답에 플러스
                    matched = True
                    break                   # 현재 빈 공간을 채웠으므로 회전 중지
                
                rotated_puzzle = rotate(rotated_puzzle) # 일치하지 않으면 90도 회전
            
            if matched:
                break # 현재 빈 공간을 채웠으므로 다음 빈 공간으로 넘어감
                
    return answer