def solution(n, tops):
  
    # i번째 아래 삼각형을 3번으로 하면, i+1번째 아래 삼각형을 2번으로 못하므로 경우의 수를 아래 2가지로 나눈다.
    a = [0] * (n+1) # 3번으로 했을 경우
    b = [0] * (n+1) # 3번 아닌 걸로 했을 경우
    m = 10007
    a[0] = 0
    b[0] = 1 # 4번으로 가능

    for idx, top in enumerate(tops): # 0~3

        if top == 1:

            a[idx+1] = (a[idx] + b[idx])% m
            b[idx+1] = (2*a[idx] + 3*b[idx])% m

        else:

            a[idx+1] = (a[idx] + b[idx]) % m
            b[idx+1] = (a[idx] + 2*b[idx])% m
            
    return (a[n] + b[n]) % m