ip_totalnum= int(input('total no. of input x:\t'))

def line():
    print('-'*50)


x_list=[]
fx_list=[]

for i in range(ip_totalnum):    
    ip_x=int(input('place value of x:\t'))
    ip_fx=eval(input('place value of f(x):\t'))
    print()
    x_list.append(ip_x)
    fx_list.append(ip_fx)
    
import math as m
sinx_list=[]
sin2x_list=[]
cosx_list=[]
cos2x_list=[]
for i in x_list:
    sin_val=m.sin(m.radians(i))
    sinx_list.append(sin_val)

    sin2_val=m.sin(2*m.radians(i))
    sin2x_list.append(sin2_val)

    cos_val=m.cos(m.radians(i))
    cosx_list.append(cos_val)

    cos2_val=m.cos(2*m.radians(i))
    cos2x_list.append(cos2_val)

    print()
   
# print(sinx_list,':sinx')    
# print(sin2x_list,':sin2x')    
# print(cosx_list,':cosx')    
# print(cos2x_list,':cos2x')    
    

fxsinx_list= [i*j for i,j in zip(fx_list,sinx_list)]
fxsin2x_list= [i*j for i,j in zip(fx_list,sin2x_list)]
fxcosx_list= [i*j for i,j in zip(fx_list,cosx_list)]
fxcos2x_list= [i*j for i,j in zip(fx_list,cos2x_list)]
print()
# print(fxsinx_list,'fxsinx')
# print(fxsin2x_list,'fxsin2x')
# print(fxcosx_list,'fxcosx')
# print(fxcos2x_list,'fxcos2x')

# print()

import statistics as st
fx_mean=st.mean(fx_list)
fxsinx_mean=st.mean(fxsinx_list)
fxsin2x_mean=st.mean(fxsin2x_list)
fxcosx_mean=st.mean(fxcosx_list)
fxcos2x_mean=st.mean(fxcos2x_list)
    
a0=2*(fx_mean)
b1=2*(fxsinx_mean)
b2=2*(fxsin2x_mean)
a1=2*(fxcosx_mean)
a2=2*(fxcos2x_mean)
    
y_list=[]
for x in x_list:
    f_of_x = (a0/2)+a1*(m.cos(m.radians(x))) + a2*(m.cos(2*m.radians(x))) + b1*(m.sin(m.radians(x))) + b2*(m.sin(2*m.radians(x))) 
    y_list.append(f_of_x)
    
    # print(f_of_x,'y')
    # print(x,'x')


line()
print('sin(x) coloumn:\n')
for x in sinx_list:
    print(x)

line()

print('sin(2x) coloumn:\n')
for x in sin2x_list:
    print(x)

line()

print('cos(x) coloumn:\n')
for x in cosx_list:
    print(x)

line()

print('cos(2x) coloumn:\n')
for x in cos2x_list:
    print(x)

line()

print('f(x)sin(x) coloumn:\n')
for x in fxsinx_list:
    print(x)

line()

print('f(x)sin(2x) coloumn:\n')
for x in fxsin2x_list:
    print(x)

line()

print('f(x)cos(x) coloumn:\n')
for x in fxcosx_list:
    print(x)

line()

print('f(x)cos(2x) coloumn:\n')
for x in fxcos2x_list:
    print(x)

line()
print(fx_mean,'\t:f(x) mean')
print(fxsinx_mean,'\t:f(x)sinx mean')
print(fxsin2x_mean,'\t:f(x)sin2x mean')
print(fxcosx_mean,'\t:f(x)cosx mean')
print(fxcos2x_mean,'\t:f(x)cos2x mean')

line()
print(a0, '\t:a0')
print(a1, '\t:a1')
print(a2, '\t:a2')
print(b1, '\t:b1')
print(b2, '\t:b2')

line()
print('values of x -- f(x) for plotting graph')
print(x_list,'x')    
print(fx_list,'f(x)') 





# plot
import matplotlib.pyplot as plt

plt.plot(x_list,y_list)
# plt.axis([0, 6, 0, 20])
plt.show()


inpo=input()
