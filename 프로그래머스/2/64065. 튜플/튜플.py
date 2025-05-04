def solution(s):

    import re

    from collections import Counter

    cnt_dic = Counter(re.findall(r'\d+', s)).most_common()

    return [int(k) for k, v in cnt_dic]