def solution(my_string):
    for char in my_string:
        remove="aeiou"
    return my_string.translate(str.maketrans('', '', remove))