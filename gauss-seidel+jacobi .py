# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 18:54:28 2020

@author: shubham
"""


import numpy
m=int(input("number of equations:\n"))
n=int(input('number of variables:\n'))
g=input('type gs for gauss seidel iterative method\n type gj for gauss jacobi iterative method\n:')
matrix = numpy.zeros((m,n))
x=numpy.zeros((m))

vector=numpy.zeros((n))


for a in range(0,m):
    for b in range(0,n):
        matrix[a,b]=float(input(f"Element a[{str(a+1)+str(b+1)}]:\n"))
    vector[a]=float(input(f"b[{str(a+1)}]:\n"))
ite=eval(input('number of iterations:\n'))

if g=='gs' or g== "GS" or g=="Gs" or g=='gS':
    for c in range(ite):
        s=0
        for d in range(m):
            s=0
            for e in range(n):
                if e!=d:
                    s+= matrix[d,e]*x[e]
            x[d]=(vector[d]-s)/matrix[d,d]
            print(f"x[{d}]:{x[d]}")
        print("iterations: ",c+1)
        

elif g=='gj' or g== 'GJ' or g=='Gj' or g=='gJ':
    for c in range(ite):
        s=0
        for d in range(m):
            s=0
            for e in range(n):
                if e!=d:
                    s= matrix[d,e]*x[e]
            x[d]=(vector[d]-s)/matrix[d,d]
            print(f"x[{d}]:{x[d]}")
        print("iterations: ",c+1)

else:
    print('pls type method correctly')