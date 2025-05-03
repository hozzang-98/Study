from collections import Counter
import re

def make_multiset(s):
    s = s.lower()
    return [s[i:i+2] for i in range(len(s)-1) if re.match("^[a-zA-Z]{2}$", s[i:i+2])]

def solution(str1, str2):
    str1_multiset = make_multiset(str1)
    str2_multiset = make_multiset(str2)

    counter1 = Counter(str1_multiset)
    counter2 = Counter(str2_multiset)

    intersection = sum((counter1 & counter2).values())
    union = sum((counter1 | counter2).values())

    return 65536 if union == 0 else int(intersection / union * 65536)