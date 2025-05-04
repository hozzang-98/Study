def solution(record):

    answer = []
    dic = {}

    for rec in record:

        if 'Enter' in rec or 'Change' in rec:

            dic[rec.split()[1]] = rec.split()[2]

    for rec in record:

        if 'Enter' in rec:

            answer.append("{}님이 들어왔습니다.".format(dic[rec.split()[1]]))

        elif 'Leave' in rec:

            answer.append("{}님이 나갔습니다.".format(dic[rec.split()[1]]))

    return answer