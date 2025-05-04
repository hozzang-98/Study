def solution(h1, m1, s1, h2, m2, s2):
    
    answer = 0

    # 시작시간과 끝시간을 초단위로 변환
    startTime = h1 * 3600 + m1 * 60 + s1
    endTime = h2 * 3600 + m2 * 60 + s2  

    # next기준으로 계산할거니 포함되지 않는 시작시간 00시, 12시 미리 카운팅
    if (startTime == 0 * 3600) or (startTime == 12 * 3600):
        answer += 1

    while startTime < endTime:

        # 시침은 1시간에 30도 1분에 0.5도 1초에 1/120도
        hcurAngle = startTime * 1/120 % 360
        # 분침은 1분에 6도 1초에 0.1도 
        mcurAngle = startTime * 0.1 % 360
        # 초침은 1초 6도
        scurAngle = startTime * 6 % 360

        if (startTime + 1) * 1/120 % 360 == 0:
            
            hNextAngle = 360
            
        else:
            
            hNextAngle = (startTime + 1) * 1/120 % 360
            
        if (startTime + 1) * 0.1 % 360 == 0:
            
            mNextAngle = 360
            
        else:
            
            mNextAngle = (startTime + 1) * 0.1 % 360
            
        if (startTime + 1) * 6 % 360 == 0:
            
            sNextAngle = 360
            
        else:
            
            sNextAngle = (startTime + 1) * 6 % 360

        # hNextAngle = 360 if (startTime + 1) * 1 / 120 % 360 == 0 else (startTime + 1) * 1 / 120 % 360
        # mNextAngle = 360 if (startTime + 1) * 0.1 % 360 == 0 else (startTime + 1) * 0.1 % 360
        # sNextAngle = 360 if (startTime + 1) * 6 % 360 == 0 else (startTime + 1) * 6 % 360
        
        if (scurAngle < hcurAngle) & (sNextAngle >= hNextAngle):

            answer += 1
            
        if (scurAngle < mcurAngle) & (sNextAngle >= mNextAngle):

            answer += 1

        if (sNextAngle == hNextAngle) & (hNextAngle == mNextAngle):

            answer -= 1

        startTime += 1
    
    return answer