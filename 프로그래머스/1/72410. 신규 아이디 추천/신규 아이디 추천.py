import re

def solution(new_id):
    # 1단계: 소문자로 변환
    new_id = new_id.lower()

    # 2단계: 허용된 문자만 남기기
    new_id = re.sub(r"[^a-z0-9\-\_\.]", "", new_id)

    # 3단계: 연속된 마침표를 하나로 변환
    new_id = re.sub(r"\.{2,}", ".", new_id)

    # 4단계: 마침표가 처음이나 끝에 위치하면 제거
    new_id = new_id.strip(".")

    # 5단계: 빈 문자열이면 "a" 대입
    if not new_id:
        new_id = "a"

    # 6단계: 길이가 16자 이상이면 15자로 줄이고, 마지막 문자가 "."이면 제거
    new_id = new_id[:15].rstrip(".")

    # 7단계: 길이가 2 이하라면 마지막 문자를 반복해서 붙이기
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id