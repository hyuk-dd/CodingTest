# def solution(wallet, bill):
#     cnt = 0
#     bill.sort()
#     wallet.sort()
#     while True:
#         if wallet[0] < bill[0] or wallet[1] < bill[1]:
#             # print('원본', bill)
#             bill[1] //= 2
#             bill.sort()
#             cnt += 1
#             # print('반접고', bill)
#         else:
#             break

#     return cnt


def solution(wallet, bill):
    cnt = 0
    while min(wallet) < min(bill) or max(wallet) < max(bill):
        bill[bill.index(max(bill))] //= 2
        cnt += 1
        
    return cnt