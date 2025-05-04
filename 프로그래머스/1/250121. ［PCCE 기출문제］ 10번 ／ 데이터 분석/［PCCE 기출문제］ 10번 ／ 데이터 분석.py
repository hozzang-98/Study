import pandas as pd

def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    
    df = pd.DataFrame(data, columns=['code','date','maximum','remain'])
    
    condition = df[ext] < val_ext
    
    conditioned_df = df[condition]
    
    answer = conditioned_df.sort_values(by=sort_by, ascending=True)
    
    answer = answer.values.tolist()
    return answer