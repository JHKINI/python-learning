a= (1,2,[12,2,3],4,5)
a[2][0] = 13
a[2][1] = 5
a[2][2] = 7
print(a)

b={1,(1,2,3),5}
print(b)

d = {1:'value','key':2}
print(type(d))
print("d[1] = ", d[1])
print("d['key'] = ", d['key'])

num_int=123
num_str="456"
print("Datatypeofnum_int:", type(num_int))
print("Datatypeofnum_strbefore Type Casting:", type(num_str))
num_str=int(num_str)
print("Datatypeofnum_strafterTypeCasting:", type(num_str))
num_sum=num_int +num_str
print("Sumofnum_intandnum_str:", num_sum)
print("Datatypeofthesum:", type(num_sum))