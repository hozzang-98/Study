def add_minutes(time, minutes):
    hour = time // 100
    minute = time % 100
    minute += minutes
    hour += minute // 60
    minute %= 60
    return hour * 100 + minute

def solution(schedules, timelogs, startday):

    answer = 0

    for schedule, timelog in zip(schedules, timelogs):
        
        current_day = startday
        sign = True

        for time in timelog:
            
            # 토,일은 Pass
            if current_day <= 5:

                latest = add_minutes(schedule, 10)

                if time > latest:

                    sign = False
                    break

            current_day += 1

            if current_day > 7: current_day = 1

        if sign:

            answer += 1

    return answer