import math
def solution(numer1, denom1, numer2, denom2):
    num=denom1*numer2+denom2*numer1
    denom=denom1*denom2
    g=math.gcd(num,denom)
    answer=[num//g,denom//g]
    return answer