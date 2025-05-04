def solution(age):

    answer = ''

    dic = {str(i):chr(i+97) for i in range(26)}

    answer = ''.join([dic[s] for s in str(age)])

    return answer