print("3"+3)
print("3"-3)
print("3"*"2")
print(3+True)
print(5+None)
print(1+None)
print("a"*2)

# TypeError: can only concatenate str (not "int") to str
# eduardo@192 py % python3
# Python 3.9.6 (default, Dec  2 2025, 07:27:58) 
# [Clang 17.0.0 (clang-1700.6.3.2)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# Cmd click to launch VS Code Native REPL
# >>> print("3"+3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
# >>> print("3"-3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for -: 'str' and 'int'
# >>> print("3"*"2")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can't multiply sequence by non-int of type 'str'
# >>> print(3+True)
# 4
# >>> print(5+None)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
# >>> print(1+None)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
# >>> print("a"*2)
# aa
# # >>> 