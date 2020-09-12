

import math as m
import sympy as sp

C=eval(input('spring constant:(in N/m)\t'))
a=eval(input('lattice constant:(in m)\t'))
mass=eval(input('mass of atom:(in kg)\t'))

q_list=[]
qaShow_list=[]
qa_list=[]
for i in range(1,101):
    q_list.append(-m.pi/(i*a))
    qaShow_list.append(-sp.pi/(i))
    qa_list.append(-m.pi/(i))
    
    
q_list.append(0)
qaShow_list.append(0)
qa_list.append(0)

for i in reversed(range(1,101)):
    q_list.append(m.pi/(i*a))
    qaShow_list.append(sp.pi/(i))
    qa_list.append(m.pi/(i))

oCo=m.sqrt((4*C)/mass)

sin_list=[]
omega_list=[]

for x in qa_list:
    sin_list.append(m.sin(m.radians(x/2)))
    omega_list.append(oCo* abs(m.sin(m.radians(x/2))))    
    
# print('q-list:\n',q_list)
# print('qa-list:\n',qaShow_list)
# print('sin-list:\n',sin_list)
# print('omega-list:\n',omega_list)
def line():
    print('-'*30)
    
line()    
print('q column')  
for y in q_list:    
    print("%10.3e"% (y))
    
line()    
print('qa column')  
for y in qaShow_list:    
    print(y)
    
line()    
print('sin(qa/2) column')  
for y in sin_list:    
    print("%10.3e"% (y))
    
line()  
print('omega column')  
for y in omega_list:    
    print("%10.3e"% (y))

import matplotlib.pyplot as pl
pl.plot(q_list,omega_list)
pl.show()


# om= m.sqrt((4*C)/m) * abs(m.sin(m.radians(qa/2)))

inpo=input()