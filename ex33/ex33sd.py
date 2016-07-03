### Ex 33 Study Drills ###

def num_list(end):
	i = 0
	numbers = []
	
	while i < end:
		numbers.append(i)
		i += 1
	
	return numbers
	
print num_list(6)
print num_list(10)


def range_new(start, stop, inc):
	i = start
	numbers = []
	
	while i < stop:
		numbers.append(i)
		i += inc
	
	return numbers
	
print range_new(0,10,1)
print range_new(0,20,2)
print range_new(0,101,25)