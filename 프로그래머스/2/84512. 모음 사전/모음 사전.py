def solution(word):

    vowels = "AEIOU"  # 모음 리스트
    weights = [781, 156, 31, 6, 1]  # 각 자리의 가중치 (5⁴, 5³, 5², 5¹, 5⁰)

    index = 0
    for i, ch in enumerate(word):  # 단어의 각 문자에 대해 계산
        index += vowels.index(ch) * weights[i] + 1

    return index