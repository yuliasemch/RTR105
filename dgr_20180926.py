Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> input("Cienījamais lietotāj, lūdzu, ievadi skaitli: ")
Cienījamais lietotāj, lūdzu, ievadi skaitli: 100
100
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainigais = input("Cienījamais letotāj, lūdzu, ievadi skaitli: ")
Cienījamais letotāj, lūdzu, ievadi skaitli: 100
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 100, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainigais
100
>>> mans_mainigais = input("Cienījamais letotāj, lūdzu, ievadi skaitli: ")
Cienījamais letotāj, lūdzu, ievadi skaitli: 200
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'mans_mainigais': 200, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR1105/test1_20180926.py ===============
Cienījamais letotāj, lūdzu, ievadi skaitli: 85
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR1105/test1_20180926.py', 'mans_mainigais': 85, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR1105/test1_20180926.py ===============
Cienījamais letotāj, lūdzu, ievadi skaitli: 4
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR1105/test1_20180926.py', 'mans_mainigais': 4, '__package__': None, 'x': 16, '__name__': '__main__', '__doc__': None}
>>> 
>>> 
=============== RESTART: /home/user/RTR1105/test1_20180926.py ===============
Cienījamais letotāj, lūdzu, ievadi skaitli: 12
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR1105/test1_20180926.py', 'mans_mainigais': 12, '__package__': None, 'x': 144, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR1105/test1_20180926.py ===============
Cienījamais letotāj, lūdzu, ievadi skaitli: 14

Traceback (most recent call last):
  File "/home/user/RTR1105/test1_20180926.py", line 5, in <module>
    print("Lietotāj, Tu esi ievadījis vērtību: %d"%(mans_manigais))
NameError: name 'mans_manigais' is not defined
>>> 
=============== RESTART: /home/user/RTR1105/test1_20180926.py ===============
Cienījamais letotāj, lūdzu, ievadi skaitli: 14
Lietotāj, Tu esi ievadījis vērtību: 14
Kā arī tagad atmiņā ir arī x = 196
>>> 
=============== RESTART: /home/user/RTR1105/test1_20180926.py ===============
Cienījamais letotāj, lūdzu, ievadi skaitli: 45
Lietotāj, Tu esi ievadījis vērtību: 45
Kā arī tagad atmiņā ir arī x = 2025
>>> type(mans_mainigais)
<type 'int'>
>>> 
=============== RESTART: /home/user/RTR1105/test1_20180926.py ===============
Cienījamais letotāj, lūdzu, ievadi skaitli: 1.1
Lietotāj, Tu esi ievadījis vērtību: 1.1000
Kā arī tagad atmiņā ir arī x = 1.210
>>> 
=============== RESTART: /home/user/RTR1105/test1_20180926.py ===============
Cienījamais letotāj, lūdzu, ievadi skaitli: 1.1
Lietotāj, Tu esi ievadījis vērtību:     1.1000
Kā arī tagad atmiņā ir arī x =           1.210
>>> type(mans_mainigais)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR1105/test1_20180926.py ===============
Cienījamais letotāj, lūdzu, ievadi skaitli: 1
Lietotāj, Tu esi ievadījis vērtību:     1.0000
Kā arī tagad atmiņā ir arī x =           1.000
>>> type(mans_mainigais)
<type 'int'>
>>> 
=============== RESTART: /home/user/RTR1105/test1_20180926.py ===============
Cienījamais lietotāj, lūdzu, tekstu: 
=============== RESTART: /home/user/RTR1105/test1_20180926.py ===============
Cienījamais lietotāj, lūdzu, ievadi tekstu: aaaa

Traceback (most recent call last):
  File "/home/user/RTR1105/test1_20180926.py", line 3, in <module>
    x = mans_mainigais * mans_mainigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR1105/test1_20180926.py ===============
Cienījamais lietotāj, lūdzu, ievadi tekstu: bbbbb
Lietotāj, Tu esi ievadījis vērtību: bbbbb

Traceback (most recent call last):
  File "/home/user/RTR1105/test1_20180926.py", line 10, in <module>
    print("Kā arī tagad atmiņā ir arī x = %s"%(x))
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR1105/test1_20180926.py ===============
Cienījamais lietotāj, lūdzu, ievadi tekstu: bbbb
Lietotāj, Tu esi ievadījis tekstu: bbbb

Traceback (most recent call last):
  File "/home/user/RTR1105/test1_20180926.py", line 10, in <module>
    print("Kā arī tagad atmiņā ir arī x = %s"%(x))
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR1105/test1_20180926.py ===============
Cienījamais lietotāj, lūdzu, ievadi tekstu: bbbb
Lietotāj, Tu esi ievadījis tekstu: bbbb

Traceback (most recent call last):
  File "/home/user/RTR1105/test1_20180926.py", line 10, in <module>
    print("Kā arī tagad atmiņā ir arī x = %s"%(x))
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR1105/test1_20180926.py ===============
Cienījamais lietotāj, lūdzu, ievadi tekstu: bbbb
Lietotāj, Tu esi ievadījis tekstu: bbbb
>>> 

