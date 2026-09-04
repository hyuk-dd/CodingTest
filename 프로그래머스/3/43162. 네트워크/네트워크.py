def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            answer += 1
        
            todo = [i]
            while todo:     # 리스트가 비어있으면 중단됨
                now = todo.pop()
                if visited[now]:
                    continue
                
                visited[now] = True
                
                for j in range(n):
                    if now != j and computers[now][j] == 1 and not visited[j]:
                        todo.append(j)
                    
    return answer