#exponential function
'''
from scipy import special as sp
s = sp.exp10(3)
print(s)
x = sp.exp2(6)
print(x)
'''


#exponential function
'''
from scipy import special as sp
si = sp.sindg(90)
print(si)
co = sp.cosdg(80)
print(co)
'''


#perm comb function ---- permutation combination
'''
from scipy import special as sp
p = sp.perm(10, 3, exact=True)
print(p)
c = sp.comb(10, 3, exact=True)
print(c)
print(dir(sp))
'''



#integration
'''
from scipy import integrate as igt
f = lambda x: x**3
i = igt.quad(f, 1, 2)  #syntax: (function, lower limit, upper limit)
print(i)
'''



#polynomial function
from numpy import poly1d
p = poly1d([3,4,0,8], variable = 'z')
print(p)



























