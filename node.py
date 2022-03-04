print(5//8)
print(5%8)
print(5**8)
print(divmod(9,4))
print((1+2j)+2+3j)
print("===========")
import math
from pickle import PERSID
a = math.sqrt(2)
print(a)
print("%6.2f"%(a))
print('{} is {:.2f}'.format(a,a))
print(f'{a} is {a:.2f}')
print("===========")
import cmath
a = cmath.sqrt(1+2j)
print(a)
print("===========")
age = 23
message = "Happy" +str(age)+ "rd Birthday!"
print(message)
print("===========")
print('姓名：','张三')
print('姓名：','张三',end='\t')
print('hello',2022,sep=',')
print("===========")
a='init'
b=7.8378
print('my name is %s and the number is %0.2f' % (a,b))
print('my name is {} and the number is {}' .format(a,b))
print('my name is {0} and the number is {1:2f}' .format(a,b))
print('{1}, my name is {0}! {1}! ' .format('init','hello'))
print("{my name} s age is {myage}" .format(myname=a,myage=20))
print("===========")
person =['init' ,20]
print("{0[0]} s age is {0[1]}".format(person))
print("{person[0]} s age is {person[1]}".format(person=person))