def fun(n):
a=n[0]
b=n[-1]
list1=[a,b]
return list1

list2=[2,3,4,5]
fun(list2)
n=fun(list2)
print(n)

def fun2(x):
for i in x:
if i < 5:
print (i)
fun2(list2)
x=fun2(list2)
print(x)

