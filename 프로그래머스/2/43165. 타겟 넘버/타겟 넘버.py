def solution(numbers, target):
    leaves = [0]
    for num in numbers:
        tmp = []
        for leaf in leaves:
            tmp.append(leaf + num)
            tmp.append(leaf - num)
        leaves = tmp
        
    return leaves.count(target)
