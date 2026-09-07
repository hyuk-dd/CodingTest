def solution(numbers, target):
    # 첫 시작은 합계 0에서 출발
    leaves = [0]
    
    for num in numbers:
        tmp = []
        # 이전 단계까지 만들어진 모든 합계(leaf)들에 대해 현재 숫자(num)를 더하고 뺌
        # print(num)
        for leaf in leaves:
            # print("leaf:", leaf)
            tmp.append(leaf + num)
            tmp.append(leaf - num)
            # print("tmp:", tmp)
        # 다음 단계를 위해 leaves 갱신
        leaves = tmp
        # print("leaves:", leaves)
        
    # 모든 숫자를 연산한 최종 결과 리스트에서 target과 일치하는 개수를 셈
    return leaves.count(target)