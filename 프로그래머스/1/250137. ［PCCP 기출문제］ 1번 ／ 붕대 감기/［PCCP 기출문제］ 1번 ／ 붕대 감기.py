from collections import deque


def solution(bandage, health, attacks):
    '''
    - 1초 마다의 상황으로 접근하는 풀이
    - 최대 체력과 현재 체력을 구분하여 선언
    - 연속으로 붕대를 감는 데 성공한 시간을 tt로 선언 -> 이후 t초 만큼 성공하면 y만큼 추가 회복하기 위해서
    - 가장 가까운 시간 대의 공격부터 비교하고 적용하기 위해 deque 선언 후 popleft 사용
    - attack: 다음 당할 공격
    '''
    full_hp = health
    tt = 0
    attacks = deque(attacks)    
    attack = attacks.popleft()

    # 1초 마다 상황 비교, 0초는 초기 상태이므로 1초부터 시작
    # 공격 시간을 기준으로 attacks가 오름차순 정렬되어 있으므로 마지막에 있는 요소의 공격 시간만큼 상황(초) 반복
    for time in range(1, attacks[-1][0]+1):
        tt += 1    # 연속으로 붕대 감는 데 성공한 경우
        
        # 다음 당할 공격(attack)과 시간이 같아졌을 경우 공격을 당한다
        # 현재 체력에서 피해량 만큼 감소
        # 공격 당하면 연속 붕대 성공도 0으로
        if attack[0] == time:
            health -= attack[1]    
            tt = 0
            # 아직 남은 공격이 있다면 다음 당할 공격에 popleft() 하여 저장
            if attacks:
                attack = attacks.popleft()
                
        # 공격 당하지 않는 상황이라면
        else:
            # 현재 체력이 최대 체력이 아니라면 초당 회복(x) 진행
            if health != full_hp:
                health += bandage[1]
            # 연속 성공 시간이 t초 시전 시간과 같아졌다면 추가 회복(y) 진행
            if tt == bandage[0]:
                health += bandage[2]
                tt = 0    # 추가 회복 했으니까 다시 0으로
        
        # 회복을 진행하고 나서 만약 현재 체력이 최대 체력보다 크다면
        # 현재 체력을 다시 최대 체력으로 조정
        if health > full_hp:
            health = full_hp
        # 체력이 0이 되면 -1 반환
        if health <= 0:
            return -1
    return health
