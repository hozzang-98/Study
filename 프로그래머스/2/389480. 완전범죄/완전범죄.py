def solution(info, n, m):
    dp = {0: 0}  # A의 누적 흔적: 최소 B의 누적 흔적
    step = 0

    for a_trace, b_trace in info:
        print(f"\n[STEP {step}] 현재 물건 = A:{a_trace}, B:{b_trace}")
        next_dp = dict()

        for a_sum, b_sum in dp.items():
            # A가 훔치는 경우
            new_a = a_sum + a_trace
            if new_a < n:
                print(f"  - A가 훔친다면: A누적 {new_a}, B누적 {b_sum}")
                if new_a not in next_dp:
                    next_dp[new_a] = b_sum
                    print(f"    → 처음 등장: next_dp[{new_a}] = {b_sum}")
                else:
                    if b_sum < next_dp[new_a]:
                        print(f"    → 더 작은 B 흔적 발견: 기존 {next_dp[new_a]} → 새 {b_sum}")
                    next_dp[new_a] = min(next_dp[new_a], b_sum)

            # B가 훔치는 경우
            new_b = b_sum + b_trace
            if new_b < m:
                print(f"  - B가 훔친다면: A누적 {a_sum}, B누적 {new_b}")
                if a_sum not in next_dp:
                    next_dp[a_sum] = new_b
                    print(f"    → 처음 등장: next_dp[{a_sum}] = {new_b}")
                else:
                    if new_b < next_dp[a_sum]:
                        print(f"    → 더 작은 B 흔적 발견: 기존 {next_dp[a_sum]} → 새 {new_b}")
                    next_dp[a_sum] = min(next_dp[a_sum], new_b)

        dp = next_dp
        print(f"[STEP {step} 결과 dp]: {dp}")
        step += 1

        if not dp:
            print("→ 더 이상 유효한 선택지 없음 (잡힘)")
            return -1

    min_a = min((a for a, b in dp.items() if b < m), default=-1)
    print(f"\n✅ 최종 최소 A의 흔적: {min_a}")
    return min_a