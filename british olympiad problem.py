#problem is statement of this link: https://youtu.be/0Hl75Pap6iY

#----------------------------------------------------------------------
""" first code : with branchless programming and list comprihension (lil bit advance than basic python) """


import math 
ls=[i*(math.sqrt(i)-math.floor(math.sqrt(i))==0) for i in range(99_999, 100_00_00)]

r=list(filter(lambda x: x!=0,ls))
rl=[x*(x!=0) for x in r]

main = [i*(int(str(i)[:3])+1==int(str(i)[3:])) for i in rl]
        
fin=r=list(filter(lambda x: x!=0,main))
print(fin)

#--------------------------------------------------------------------------------
""" second code : same code with no branchless programming and list comprehension"""

import math 
ls=[]
for i in range(99999,1000000):
    sr=math.sqrt(i)
    x= sr-math.floor(sr)
    if x==0:
        ls.append(i)

main=[]
for y in ls:

    s13= str(y)[:3]
    s23= str(y)[3:]
    int1=int(s13)
    int2=int(s23)
    if int1+1==int2:
        main.append(y)
print(main)      
