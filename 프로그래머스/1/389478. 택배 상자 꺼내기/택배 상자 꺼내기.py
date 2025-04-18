def solution(n, w, num):
    boxes = [[] for _ in range(w)]
    box_num = 1
    left_to_right = True

    while box_num <= n:
        if left_to_right:
            for i in range(w):
                if box_num > n:
                    break
                boxes[i].append(box_num)
                box_num += 1
        else:
            for i in range(w - 1, -1, -1):
                if box_num > n:
                    break
                boxes[i].append(box_num)
                box_num += 1
        left_to_right = not left_to_right

    # 꺼내야 할 상자의 위치 탐색
    for column in boxes:
        if num in column:
            return len(column) - column.index(num)

    return 0