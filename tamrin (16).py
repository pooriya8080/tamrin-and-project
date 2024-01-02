import math as m

def test(x,y):

    z = m.sin(x) / m.cos(x)

    r=z*m.sin(y)

    return(r)

print(test(5,6))
