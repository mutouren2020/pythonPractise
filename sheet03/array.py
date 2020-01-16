names = ['tianxiaoqi', 'wangxiaoer', 'zhangxiaosan']
print(names[0].title())
print(names[-1].title())

names[0] = 'mutouren'
print(names)

names.append("mayun")
print(names)

names.insert(1,"xiaoyaozi")
print(names)

del names[0]
print(names)

print(names.pop())
print(names)

print(names.pop(1))
print(names)

msg = 'xiaoyaozi'
names.remove('xiaoyaozi')
print(msg)

