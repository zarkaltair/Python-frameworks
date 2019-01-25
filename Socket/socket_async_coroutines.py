# from inspect import getgeneratorstate


def coroutine(func):
	def inner(*args, **kwargs):
		g = func(*args, **kwargs)
		g.send(None)
		return g
	return inner


def subgen():
	x = 'Ready to accept message'
	message = yield x
	print('Subgen received:', message)

# g = subgen()
# print(getgeneratorstate(g))

# g.send(None) # or next(g)
# print(getgeneratorstate(g))

# g.send('Ok')
# print(getgeneratorstate(g))


class BlaBlaException(Exception):
	pass


@coroutine
def average():
	count = 0
	summ = 0
	average = None

	while True:
		try:
			x = yield average
		except StopIteration:
			print('Done')
			break
		except BlaBlaException:
			print('...................')
			break
		else:
			count += 1
			summ += x
			average = round(summ / count, 2)

		return average