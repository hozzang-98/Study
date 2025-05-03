from itertools import combinations

def solution(relation):
    n_cols = len(relation[0])
    n_rows = len(relation)
    candidates = []

    for i in range(1, n_cols + 1):
        for comb in combinations(range(n_cols), i):

            # 유일성 빠르게 체크
            seen = set()
            is_unique = True
            for row in relation:
                key = tuple(row[idx] for idx in comb)
                if key in seen:
                    is_unique = False
                    break
                seen.add(key)

            if not is_unique:
                continue

            # 최소성 검사
            comb_set = set(comb)
            if any(prev.issubset(comb_set) for prev in candidates):
                continue

            candidates.append(frozenset(comb))  # 불변 set으로 저장

    return len(candidates)