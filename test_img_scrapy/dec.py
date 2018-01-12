INT=4

def getcode():
	if INT == 1:
		return '3'
	else:
		return '2'


def dec(level):
	print ('nice')
	def in_fun(func):
		def in_dec():
			print ('in')
			if level == '1':
				func('程度1')
			elif level == '2':
				func('程度2')
			elif level == '3':
				func('程度3')
			else:
				func('程度其它')
		return in_dec
	return in_fun

@dec('')
def begin(info):
	print ('start',info)

begin()
