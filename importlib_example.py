import importlib    #python提供importlib作为标准库的一部分      函数（function）类（class）> 模块module>包package>库library   个人理解，有待验证

'''
作用：通过字符串str导入模块，类 (dynamic动态导入,模块运行时才导入)
path = 'aaa.bbb'

#print(path.split('.'))
#print(path.rsplit('.'))

a,b = path.split('.')   #python内置切片函数      path.split()   返回一个列表

print(a)
print(b)
print(type(a))

c,d = ['a',1]
print(c)
'''

path = 'settings.SettingA'

m,c = path.split('.')

r = importlib.import_module(m)    #importlib模块import_module函数（）调用call返回一个模块    通过print(type(r))可知
#x = r.__repr__()           
#print(x)
#y = r.__str__()
#print(y)
print(r)
print(type(r))
print(getattr(r,c))    #取r对象的c属性

cls = getattr(r,c)
x = cls()
print(x.debug)




