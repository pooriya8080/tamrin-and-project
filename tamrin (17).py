import math as m

def test(x,y,t):

    h=x- y

    r=h/t

    w=m.sqrt(r)

    return(w)

print(test(9,4,3))
