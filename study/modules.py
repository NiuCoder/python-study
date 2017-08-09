# -*- encoding:utf-8 -*-
import fibo    # this is equivalent to "from fibo import *"
# single function can be imported like this :"from fibo import fib" 这是动态引入，不会占用local symbol table
print fibo.fib(1000)
print fibo.fib2(1000)

print fibo.__name__

fib = fibo.fib
print fib(500)

print dir(fibo)



