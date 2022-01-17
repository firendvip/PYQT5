# class A:
#     def __init__(self):
#         print('A')
#
# class B(A):
#     def __init__(self):
#         print('B')
#
#
# class C(A):
#     def __init__(self):
#         super().__init__()
#         print('C')
#
# A1 = A()
# B1 = B()
# print()
# C1 = C()

#  单例设计模式：
#  这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。
#  这种模式涉及到一个单一的类，该类负责创建自己的对象，同时确保只有单个对象被创建。
#  这个类提供了一种访问其唯一的对象的方式，可以直接访问，不需要实例化该类的对象。

# 意图：保证一个类仅有一个实例，并提供一个访问它的全局访问点。
#
# 主要解决：一个全局使用的类频繁地创建与销毁。
#
# 何时使用：当您想控制实例数目，节省系统资源的时候。
#
# 如何解决：判断系统是否已经有这个单例，如果有则返回，如果没有则创建。
#
# 关键代码：构造函数是私有的。

# https://www.runoob.com/design-pattern/singleton-pattern.html

# href在是CSS代码的一种意思是指定超链接目标的URL。
# 在HTML和JSP页面代码里的作用是标签，其作用是插入一个超链接，
# “#”是默认当前页面，可以把#换成想跳转的页面。

# lambda 表达式 如果一个函数的函数体仅有 1 行表达式，则该函数就可以用 lambda 表达式来代替。
# def add(x, y):
#     return x+ y
# print(add(3,4))
#
# ass = lambda x,y:x+y # lambda 参数:F(x) (返回结果)
# print(ass(3,4))

