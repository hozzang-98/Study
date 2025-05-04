def time_change(hhmm):
    mins, secs = map(int, hhmm.split(':'))
    return mins * 60 + secs

def in_opening(pos, op_start, op_end):
    
    if op_start <= pos <= op_end:
            
        pos = op_end 

    return pos

def solution(video_len, pos, op_start, op_end, commands):
    
    answer = ''
    
    command_dic = {"next":10, "prev":-10}
    
    pos = time_change(pos)
    op_start = time_change(op_start)
    op_end = time_change(op_end)
    video_len = time_change(video_len)

    for command in commands:
        
        pos = in_opening(pos, op_start, op_end)
        
        pos += command_dic[command]

        if pos <= 0: pos = 0
        
        elif pos >= video_len: pos = video_len
        
        pos = in_opening(pos, op_start, op_end)
        
    m = str(pos // 60) if len(str(pos // 60)) == 2 else '0' + str(pos // 60)
    s = str(pos % 60) if len(str(pos % 60)) == 2 else '0' + str(pos % 60)
        
    
    return '{}:{}'.format(m,s)