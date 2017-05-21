


##########
# Herencia
###########

class A:
	def a(self):
		print("A")
class B(A):
	def a(self):
		print("B")
class C(A):
	def a(self):
		print("C")
class D(B,C):
	def llamaA(self):
		super().a()
	def llamaAbuelo(self):
		super(C,self).a()

obj=D()
obj.llamaA()
obj.a()
obj.llamaAbuelo()
print("MRO:",D.__mro__)


