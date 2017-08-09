s = set([1,2,1,3,4,2])

print s

s.add(5)

print s

s.remove(2)

print s

s1 = set([1,2,3])
s2 = set([2,3,4])
print s1 & s2
print s1 | s2

# create a set
basket = ['apple','orange','apple','pear','orange','banana']
fruit = set(basket)
print 'apple' in basket
print fruit

# fast member testing
print 'orange' in fruit

# set operations
a = set('abracadabra')
b = set('alacazam')
print a
print a - b    # letters in a but not in b
print a | b    # letters in either a or b
print a & b    # letters in both a and b
print a ^ b    # letters in a or b but not both

