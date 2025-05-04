def slope(dot1, dot2):

    x1, y1 = dot1
    x2, y2 = dot2
    
    return float('inf') if x1 == x2 else (y2 - y1) / (x2 - x1)

def solution(dots):

    # 가능한 모든 직선 조합에서 기울기가 같은 경우를 찾음
    pairs = [
        (dots[0], dots[1], dots[2], dots[3]),
        (dots[0], dots[2], dots[1], dots[3]),
        (dots[0], dots[3], dots[1], dots[2])
    ]
    
    for dot1, dot2, dot3, dot4 in pairs:
    
        if slope(dot1, dot2) == slope(dot3, dot4):
            return 1
            
    return 0