Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print(123)
123
>>> print(98.6)
98.6
>>> print('Helo world')
Helo world
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> x=12.2
>>> x
12.2
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 12.2, '__name__': '__main__', '__doc__': None}
>>> y=14
>>> y
14
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 12.2, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> x=100
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> x1q3z9ocd = 35.0
>>> a

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x1q3z9afd = 12.50
>>> b

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> x1q3z9ocd = 35.0 
x1q3z9afd = 12.50
x1q3p9afd = x1q3z9ocd * x1q3z9afd
print(x1q3p9afd)
>>> a

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=
SyntaxError: invalid syntax
>>> a=35.0
>>> a
35.0
>>> b=12.50
>>> b
12.5
>>> c=a*b
>>> c
437.5
>>> print(c)
437.5
>>> vars()
{'a': 35.0, 'c': 437.5, 'b': 12.5, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x1q3z9afd': 12.5, 'x': 100, 'y': 14, '__name__': '__main__', '__doc__': None, 'x1q3z9ocd': 35.0}
>>> x=2
>>> x
2
>>> x=x+2
>>> x
4
>>> print(x)
4
>>> x=3.9*x*(1-x)
>>> x
-46.8
>>> x=0.6
>>> x=3.9*x*(1-x)
>>> x
0.9359999999999999
>>> x=3.9*x*(1-x)
>>> x
0.2336256000000002
>>> xx=2
>>> xx=xx+2
>>> x
0.2336256000000002
>>> xx
4
>>> print(xx)
4
>>> yy=440*12
>>> print(yy)
5280
>>> zz=yy/1000
>>> print(zz)
5
>>> jj=23
>>> kk=jj%5
>>> print(kk)
3
>>> print(4**3)
64
>>> x=1+2*3-4/5**6
>>> x
7
>>> 1+2**3/4*5
11
>>> ddd=1+4
>>> print(ddd)
5
>>> eee='hello'+'there'
>>> print(eee)
hellothere
>>> eee='hello' + 'there'
>>> print(eee)
hellothere
>>> eee=eee+1

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    eee=eee+1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(eee)
<type 'str'>
>>> 
>>> xx=1
>>> type(xx)
<type 'int'>
>>> temp=98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type4(1.0)

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    type4(1.0)
NameError: name 'type4' is not defined
>>> type(1.0)
<type 'float'>
>>> print(float(99)+100)
199.0
>>> i=42
>>> type(i)
<type 'int'>
>>> f=float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10/2)
5
>>> print(9/2)
4
>>> print(10.0/2.0)
5.0
>>> print(99.0/100.0)
0.99
>>> sval='123'
>>> type(sval)
<type 'str'>
>>> print(sval+1)

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    print(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival=int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival+1)
124
>>> nsv='hello bob'
>>> niv=int(nsv)

Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    niv=int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> nam=input('Who are you?'°
	  
SyntaxError: invalid syntax
>>> input('Who are you?')
Who are you?

Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    input('Who are you?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> print('Welcome'nam)
SyntaxError: invalid syntax
>>> nam=input('Who are you?')
Who are you?

Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> nam=input('Who are you?')
Who are you?Chuck

Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> nam=input('Who are you?')
Who are you? Chuck

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> nam=input
('Who are you?') print('Welcome',nam)
>>> 
>>> nam=input('Who are you?') print('Welcome',nam)
SyntaxError: invalid syntax
>>> nam=input('Who are you?')
Who are you? Chuck

Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> nam=input('Who are you?')
Who are you? print('Welcome',nam)

Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 1
    print('Welcome',nam)
        ^
SyntaxError: invalid syntax
>>> inp=input('Europe floor?'°
	  
SyntaxError: invalid syntax
>>> inp=input('Europe floor?')
Europe floor?usf=int(inp)+1

Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    inp=input('Europe floor?')
  File "<string>", line 1
    usf=int(inp)+1
       ^
SyntaxError: invalid syntax
>>> inp=input('Europe floor?')
usf=int(inp)+1
print('US floor',usf)
Europe floor?0
>>> 
>>> inp=input('Europe floor?')
usf=int(inp)+1
print('US floor',usf)
Europe floor?0
>>> 
>>> US floor
SyntaxError: invalid syntax
>>> nam=input('Who are you?')
print('Welcome',nam)
Who are you?Chuck

Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    nam=input('Who are you?')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> nam=raw_input('Who are you?')
Who are you? print('Welcome',nam)
Who are you?Chuck
>>> 
>>> inp=raw_input('Europe floor?')
usf=int(inp)+1
Europe floor?0
>>> inp=raw_input('Europe floor?')
usf=int(inp)+1pri
Europe floor?0
>>> inp=raw_input('Europe floor?')
usf=int(inp)+1
print('US floor',usf)
Europe floor?0
>>> inp=raw_input('Europe floor?')
usf=int(inp)+1
print('US floor', usf)
Europe floor? 0
>>> usf

Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    usf
NameError: name 'usf' is not defined
>>> inp=raw_input('Europe floor?')
usf=int(inp)+1
print('US floor',usf)
Europe floor?0
>>> print

>>> print('US floor',usf)

Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    print('US floor',usf)
NameError: name 'usf' is not defined
>>> print('US floor')
US floor
>>> usf=int(inp)+1
>>> US floor
SyntaxError: invalid syntax
>>> inp=raw_input('Europe floor?')
usf=int(inp)+1
print('US floor',usf)
Europe floor? 0
>>> inp=raw_input('Europe floor?')
usf=int(inp)+1
print('US floor',usf)
Europe floor? 0
>>> 
=================== RESTART: /home/user/RTR105/tests_1.py ===================
Europe floor?0
('US floor', 1)
>>> 
>>> 


