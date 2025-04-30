import math
    
def solution(w,h):
    
    gcd = math.gcd(w,h)
    w_ = w / gcd
    h_ = h / gcd
    
    return w * h - gcd * (w_ + h_ - 1)
