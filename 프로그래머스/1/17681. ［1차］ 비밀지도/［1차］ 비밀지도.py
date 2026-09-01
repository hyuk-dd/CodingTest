def solution(n, arr1, arr2):
    answer = []

    li_tot_1 = []
    li_tot_2 = []
    # b = 20
    # print(9 & 2)
    for i in arr1:
        li_1 = []
        num = i
        for _ in range(n):
            # if 
            li_1.append(num % 2)
            num //= 2
            # print(b)
    # print(a)
        li_1.reverse()
        li_tot_1.append(li_1)
    # print(a)
    print(li_tot_1)
    
    for i in arr2:
        li_2 = []
        num = i
        for _ in range(n):
            # if 
            li_2.append(num % 2)
            num //= 2
            # print(b)
    # print(a)
        li_2.reverse()
        li_tot_2.append(li_2)
    print(li_tot_2)
    
    for i in range(n):
        ans = ''
        for j in range(n):
            
            if li_tot_1[i][j] | li_tot_2[i][j] == 0:
                ans += ' '
            else:
                ans += '#'
            # print(ans)
        answer.append(ans)
    return answer