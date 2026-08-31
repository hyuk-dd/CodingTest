def solution(wallet, bill):
    cnt = 0
    bill.sort()
    wallet.sort()
    print(wallet)
    print(bill)
    # print(bill)
    while True:
        if wallet[0] < bill[0] or wallet[1] < bill[1]:
            print('원본', bill)
            bill[1] //= 2
            bill.sort()
            cnt += 1
            print('반접고', bill)
        else:
            break
        # else:
            
    # for w, h in wallet:
    #     print(w)
    #     print(h)
    return cnt