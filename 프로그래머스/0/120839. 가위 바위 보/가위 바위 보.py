def solution(rsp):
    answer = ''
    result={'0':'5','2':'0','5':'2'}
    for i in rsp:
        answer+=result.get(i)
    return answer