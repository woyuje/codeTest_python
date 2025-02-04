def solution(my_string):
    # return my_string.swapcase()
    answer=''
    for i in my_string:
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer