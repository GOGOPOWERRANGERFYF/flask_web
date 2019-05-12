#  *args 可变参数  将参数封装成一个tuple元组
#  ×kwargs 关键字参数   将参数封装成一个字典dictionary
def wrapper(func):
    def inner(*args,**kwargs):
        return func(*args,**kwargs):
    return inner
#1,无参数装饰器，执行到这一步，将下面的index函数当作参数传入wrapper函数
#2.wrapper(index) 
#3. 返回inner         
#4.index=inner    这一步 是装饰器的精髓    
@wrapper   
def index(request):
    pass


#@route装饰器url绑定view function视图函数原理
def route(url):
    def inner(func,*args,**kwargs):
        url_map['url'] = func
        #return url
    return inner
#1.先执行route('/index')
#2.返回inner       
# 3.@inner
# 4. index=inner(index)
@route('/index')  #带参数的装饰器decorator
def index():
    return 'index'


url_map={
    '/index':index
}

