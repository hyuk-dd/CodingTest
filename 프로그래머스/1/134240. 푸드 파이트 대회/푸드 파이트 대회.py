def solution(food):
    answer = ''
    ans = []
    for idx, v in enumerate(food):
        if idx == 0:
            pass
        else:
            ans += [str(idx)] * (v//2)

    answer += "".join(ans)
    answer += "0"
    ans.reverse()
    answer += "".join(ans)

    return answer