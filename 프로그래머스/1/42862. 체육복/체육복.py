def solution(n, lost, reserve):

    # 중복 제거 (여벌 체육복이 있지만 도난당한 경우)
    set_reserve = sorted(set(reserve) - set(lost))
    set_lost = sorted(set(lost) - set(reserve))

    for r in set_reserve:
    
        if r - 1 in set_lost:  # 앞번호 학생에게 먼저 빌려줌
        
            set_lost.remove(r - 1)
            
        elif r + 1 in set_lost:  # 없으면 뒷번호 학생에게 빌려줌
        
            set_lost.remove(r + 1)

    return n - len(set_lost)  # 체육복을 못 빌린 학생 수 제외