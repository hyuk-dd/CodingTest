def solution(s, n):
    answer = ''

    for i in s:
        new_chr_int = ord(i) + n
        if i == ' ':
            answer += i
            continue
        elif i.islower() and new_chr_int > ord('z'):
            new_chr_int -= (ord('z') - ord('a') + 1)
        elif i.isupper() and new_chr_int > ord('Z'):
            new_chr_int -= (ord('Z') - ord('A') + 1)
        answer += chr(new_chr_int)

    return answer