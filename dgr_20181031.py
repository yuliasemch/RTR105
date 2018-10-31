Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> fhand=open('mbox.txt')

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    fhand=open('mbox.txt')
IOError: [Errno 2] No such file or directory: 'mbox.txt'
>>> print(fhanf)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(fhanf)
NameError: name 'fhanf' is not defined
>>> print(fhand)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(fhand)
NameError: name 'fhand' is not defined
>>> stuff='Hello\nWorld!'
>>> stuff
'Hello\nWorld!'
>>> print(stuff)
Hello
World!
>>> stuf='X\nY'
>>> print(stuff)
Hello
World!
>>> stuff='X\nY'
>>> print(stuff)
X
Y
>>> len(stuff)
3
>>> xfile=open('mbox.txt')

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    xfile=open('mbox.txt')
IOError: [Errno 2] No such file or directory: 'mbox.txt'
>>> print(cheese)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(cheese)
NameError: name 'cheese' is not defined
>>> xfile=open('mbox.txt')

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    xfile=open('mbox.txt')
IOError: [Errno 2] No such file or directory: 'mbox.txt'
>>> xfile = open('mbox.txt')

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    xfile = open('mbox.txt')
IOError: [Errno 2] No such file or directory: 'mbox.txt'
>>> open('mbox.txt')

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    open('mbox.txt')
IOError: [Errno 2] No such file or directory: 'mbox.txt'
>>> open('RTR105/mbox.txt')
<open file 'RTR105/mbox.txt', mode 'r' at 0x7f4a4d3fb8a0>
>>> xfile=open('RTR105/mbox.txt')
>>> print(cheese)

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(cheese)
NameError: name 'cheese' is not defined
>>> fhand = open('RTR105/mbox.txt')
>>> count = 0
>>> 
=============== RESTART: /home/user/RTR105/tests4_20181031.py ===============

Traceback (most recent call last):
  File "/home/user/RTR105/tests4_20181031.py", line 1, in <module>
    fhand = open('RTR105/mbox.txt')
IOError: [Errno 2] No such file or directory: 'RTR105/mbox.txt'
>>> 
=============== RESTART: /home/user/RTR105/tests4_20181031.py ===============
('Line Count:', 7)
>>> fhand=open('mbox-short.txt')

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    fhand=open('mbox-short.txt')
IOError: [Errno 2] No such file or directory: 'mbox-short.txt'
>>> fhand=open('RTR105/mbox-short.txt')

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    fhand=open('RTR105/mbox-short.txt')
IOError: [Errno 2] No such file or directory: 'RTR105/mbox-short.txt'
>>> fhand=open('RTR105/mbox-short.txt')

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    fhand=open('RTR105/mbox-short.txt')
IOError: [Errno 2] No such file or directory: 'RTR105/mbox-short.txt'
>>> fhand=open('mbox-short.txt')
>>> 
>>> fhand=open('mbox-short.txt')
>>> fhand
<open file 'mbox-short.txt', mode 'r' at 0x7fe592a8a8a0>
>>> inp=fhand.read()
>>> print(len(inp))
26
>>> print(inp[:20])
digjsdigk
adgjdg
adg
>>> 
=============== RESTART: /home/user/RTR105/tests4_20181031.py ===============
>>> 
=============== RESTART: /home/user/RTR105/tests4_20181031.py ===============
>>> 
=============== RESTART: /home/user/RTR105/tests4_20181031.py ===============
Enter the file name: mbox.txt

Traceback (most recent call last):
  File "/home/user/RTR105/tests4_20181031.py", line 1, in <module>
    fname=input('Enter the file name: ')
  File "<string>", line 1, in <module>
NameError: name 'mbox' is not defined
>>> 
>>> 
=============== RESTART: /home/user/RTR105/tests4_20181031.py ===============
Enter the file name: mbox-short.txt

Traceback (most recent call last):
  File "/home/user/RTR105/tests4_20181031.py", line 1, in <module>
    fname=input('Enter the file name: ')
  File "<string>", line 1, in <module>
NameError: name 'mbox' is not defined
>>> 
