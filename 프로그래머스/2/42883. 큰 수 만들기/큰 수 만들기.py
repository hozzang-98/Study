def solution(number, k):

    answer = []  # 스택 역할
    
    for n in number:

        while k > 0 and answer and answer[-1] < n:  # 비교 연산 최적화

            answer.pop()
            k -= 1
            
        answer.append(n)  # 바로 문자열 추가

    return ''.join(answer[:len(answer)-k])  # 최종 숫자 반환
