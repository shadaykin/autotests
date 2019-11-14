def test(*args):
	try:
		if "@" in args[0]:
			print('a')
		else:
			print('aaa')
	except:
		print('b')
test('mailmail')