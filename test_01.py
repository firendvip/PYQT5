class A:
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        print('B')

#
class C(A):
    def __init__(self):
        super().__init__()
        print('C')

A1 = A()
B1 = B()
print()
C1 = C()

