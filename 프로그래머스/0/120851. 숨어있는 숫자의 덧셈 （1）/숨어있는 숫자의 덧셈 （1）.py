def solution(my_string):
    answer = 0
    a="123456789"
    for i in my_string:
        if i.isdigit():
            answer+=int(i)
    return answer