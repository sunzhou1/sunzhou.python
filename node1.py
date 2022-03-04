print('姓名：','张三')
print('姓名：','张三',end='\t')
print('hello',2022,sep=',')
print("===========")
a='init'
b=7.8378
print('my name is %s and the number is %0.2f' % (a,b))
print('my name is {} and the number is {}' .format(a,b))
print('my name is {0} and the number is {1:2f}' .format(a,b))
print('{1}, my name is {0}! {1} ' .format('init','hello'))
print("{myname}' s age is {myage}" .format(myname=a,myage=20))
print("===========")
person =['init' ,20]
print("{0[0]} s age is {0[1]}".format(person))
print("{person[0]} s age is {person[1]}".format(person=person))