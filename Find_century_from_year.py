def solution(year):
    if year / 100 > year // 100:
        return year//100 + 1
    else:
        return  year //100    


