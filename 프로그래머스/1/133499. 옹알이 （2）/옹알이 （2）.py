import re

def solution(babbling):
    valid_sounds = ["aya", "ye", "woo", "ma"]
    
    count = 0
    for word in babbling:
        # 연속된 같은 단어가 있는지 확인 (예: "ayaaya", "yeye" 등)
        if any(double in word for double in ["ayaaya", "yeye", "woowoo", "mama"]):
            continue
        
        # 정규표현식으로 유효한 발음만 남겼을 때 빈 문자열이 되는지 확인
        if re.sub(r"(aya|ye|woo|ma)", "", word) == "":
            count += 1
    
    return count