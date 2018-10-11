Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("heloo...")
heloo...
>>> new_list = []
for i in old_list:
    if filter(i):
        new_list.append(expressions(i))
        
SyntaxError: multiple statements found while compiling a single statement
>>> new_list = []
for i in old_list:
    if filter(i):
        new_list.append(expressions(i))
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
SyntaxError: multiple statements found while compiling a single statement
>>> n=[]
>>> for i in o:
	if filter(i):
		n.append(expressions(i))
		
