def solution(my_string, letter):
    # string=0
    # for i in my_string:
    #     my_string.replace(letter,"")
    #     string++
    # return my_string
    for char in letter:
        string = my_string.replace(char, "")
    
    return string