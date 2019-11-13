class TestA:
	a = 1
	def func_func(self):
		b = self.a+1
		print(b)

obj = TestA()
obj.func_func()