#list,可变

classmates = ['Tom','Jack',['James','Jones']]

classmates.append('Jimmy')

classmates.insert(1,'Jordan')

classmates.pop(2)

print classmates
print classmates[2]


#tuple，不可变，但是如果元素是list仍可变。所以本质是tuple元素所指向的地址不变
t = (1,2)
print t

t= ('Tom','Jack',['James','Jones'])
print t[1]

t[2][0] = 'Jordan'
t[2].append('Jimmy')

print t