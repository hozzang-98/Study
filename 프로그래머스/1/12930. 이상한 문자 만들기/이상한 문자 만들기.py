def solution(s):
    result = []
    words = s.split(' ')
    
    for word in words:
        temp = ''
        for i, c in enumerate(word):
            temp += c.upper() if i % 2 == 0 else c.lower()
        result.append(temp)

    return ' '.join(result)