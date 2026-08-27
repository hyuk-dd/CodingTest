def solution(s):
    answer = []
    prev = []

    for idx, a in enumerate(s):
        exist = [i for i, v in enumerate(prev) if v == a]
        if exist:
            near_idx = exist[-1]
            answer.append(idx - near_idx)
        else:
            answer.append(-1)
        prev.append(a)
        
    return answer