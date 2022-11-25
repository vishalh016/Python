class complexNumber:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        return self.a+other.a,self.b+other.b
n1=complexNumber(1,2)
n2=complexNumber(2,3)
print(n1+n2)

#                        Operator	Magic Method
#                        +	__add__(self, other)
#                        –	__sub__(self, other)
#                        *	__mul__(self, other)
#                        /	__truediv__(self, other)
#                        //	__floordiv__(self, other)
#                        %	__mod__(self, other)
#                        **	__pow__(self, other)
#                        >>	__rshift__(self, other)
#                        <<	__lshift__(self, other)
#                        &	__and__(self, other)
#                        |	__or__(self, other)
#                        ^	__xor__(self, other)