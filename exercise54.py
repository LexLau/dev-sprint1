# This is where Exercise 5.4 goes
# Name:Alex Lau

def is_triangle(a, b, c):
	if a >= (b + c) or b >= (a + c) or c >= (a + b):
		print 'No'
	else:
		print 'Yes'

def prompt_lengths():
	prompt1 = 'Please input 1st length\n'
	a = raw_input(prompt1)
	prompt2 = 'Please input 2nd length\n'
	b = raw_input(prompt2)
	prompt3 = 'Please input 3rd length\n'
	c = raw_input(prompt3)

	is_triangle(int(a), int(b), int(c))

prompt_lengths()