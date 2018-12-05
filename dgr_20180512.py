Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> original = "To be or not to be"
>>> type(original)
<type 'str'>
>>> original[0]
'T'
>>> original[1]
'o'
>>> ord(original[0])
84
>>> or
SyntaxError: invalid syntax
>>> bin(ord(original[0]))
'0b1010100'
>>> key = 5
>>> original[0] ^ key

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    original[0] ^ key
TypeError: unsupported operand type(s) for ^: 'str' and 'int'
>>> ord(original[0]) ^ key
81
>>> chr(ord(original[0]) ^ key)
'Q'
>>> original
'To be or not to be'
>>> key
5
>>> message = ""
>>> N = len(original)
>>> for i in range(N):
	message = message + chr(ord(original[i]) ^ key)

	
>>> message
'Qj%g`%jw%kjq%qj%g`'
>>> result = ""
>>> key1 = 6
>>> 
>>> for i in range(N):
	result = result + chr(ord(message[i]) ^ key1)

	
>>> result
'Wl#af#lq#mlw#wl#af'
>>> result = ""
>>> key1 = 5
>>> for i in range(N):
	result = result + chr(ord(message[i]) ^ key1)

	
>>> result
'To be or not to be'
>>> 
