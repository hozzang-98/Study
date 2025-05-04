def solution(s, skip, index):
    # 사용 가능한 알파벳만 필터링
    usable = [c for c in "abcdefghijklmnopqrstuvwxyz" if c not in skip]
    
    # 문자 → index 매핑을 빠르게 하기 위해 딕셔너리
    alpha_map = {c: i for i, c in enumerate(usable)}
    
    answer = ""
    for char in s:
        new_idx = (alpha_map[char] + index) % len(usable)
        answer += usable[new_idx]
    
    return answer