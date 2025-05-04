def date_to_day(x):

    year, month, day = x.split('.')

    return int(year) * 12 * 28 + int(month) * 28 + int(day)

def solution(today, terms, privacies):
    
    answer = []

    term_dic = {term.split()[0]: int(term.split()[1])*28 for term in terms}

    for idx, privacy in enumerate(privacies):

        date, type = privacy.split()

        limit = date_to_day(date) + term_dic[type]

        if date_to_day(today) < limit:

            continue

        else:

            answer.append(idx+1)
        
    return answer