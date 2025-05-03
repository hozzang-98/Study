def solution(msg):
    answer = []
    alphabet_dict = {chr(i): i - 64 for i in range(65, 91)}  # A~Z 초기 사전
    idx = 27  # 새로운 색인 번호 (A~Z까지 26개 존재)
    
    i = 0
    while i < len(msg):
        w = msg[i]  # 현재 입력
        while i + 1 < len(msg) and w + msg[i + 1] in alphabet_dict:
            w += msg[i + 1]  # 사전에 있는 가장 긴 문자열 찾기
            i += 1

        answer.append(alphabet_dict[w])  # 색인 출력

        if i + 1 < len(msg):  # 새로운 단어 추가 (입력이 남아있는 경우)
            alphabet_dict[w + msg[i + 1]] = idx
            idx += 1

        i += 1  # 다음 문자로 이동

    return answer