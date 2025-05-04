def solution(phone_book):
    phone_book = sorted(phone_book)
    for num,other in zip(phone_book,phone_book[1:]):
        if other.startswith(num):
            return False
    return True