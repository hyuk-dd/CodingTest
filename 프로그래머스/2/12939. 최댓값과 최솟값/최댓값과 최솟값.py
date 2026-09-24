def solution(s):
    num = list(map(int, s.split()))
    min_num = str(min(num))
    max_num = str(max(num))
    
    return " ".join([min_num, max_num])