#using loop
print(" LOOP..........")
newlist=[]
for i in 'ishika':
    newlist.append(i)
print(newlist)

#list comprehension
print('\n list comprehension.....')
newlist=[i for i in 'sangeetha']
print(newlist)

#lambda
print('\nlambda....')
z=lambda a,b,c,d:a*b*c*d
print(z(1,2,3,4))

#lambda function try 1
print('\n lambda function1....')
def func(i):
    return lambda a:a*i
z=func(2)
print(z(10)) 

#lambda function try 2
print('\n lambda function2....')
def func():
    return lambda a,b,c,d:a*b*c*d
z=func()
print(z(1,2,3,4))

#map
print("\n Map....")
def map_fun(a):
    #print(a)
    return len(a)
x=map(map_fun,('ishika','aarush','sangeetha','anjali'))
print(x)
print(list(x))      
    

#Lambda func inside List
print('\n using Lambda function inside List...')
l=list(map(lambda x: x, 'HelloPython'))
print(l)

#if in list
print("\n list....")
num=[]
for x in range(20):
    if x % 2== 0:
      num.append(x)
print(num)
print('\n conditional stmt...')
num = [ x for x in range(20) if x % 2 == 0]
print(num)
num1=[x for x in range(100) if x%2==0 if x%5==0]
print(num1)

#if else
print('\n if else...')
obj=[]
for i in range(10):
    if i%2==0:
        obj.append("Even")
    else:
        obj.append("Odd")
print(obj)
print('\n using listcomp')
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)

#list in list
print('\n list in list')
m = [[10, 20, 30, 40], [40, 50, 60, 80]]
print(m[0])
print(m[0][2])

#transpose of matrix
print("\n Transpose of matrix")
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8],[11,12,13,14]]
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
print('\n transpose using listcomp')
matrix = [[1, 2,3,4], [4,5,6,8],[11,12,13,14]]
transpose = [[row[i] for row in matrix] for i in range(4)]
print (transpose)

#filter
print("filter function")

