import re

patterns = {
	"oneOrMore": '+',
	"oneOrMoreLazy": '+?',
	"zeroOrMore": '*',
	"zeroOrMoreLazy": '*?',
	"optional": '?',
	"start_of_input": '^',
	"end_of_input": '$',
}

def to_regex(*args):
	pattern = ''.join(args)
	# TODO compile or check for validity or something
	return pattern

def from_regex(pattern):
	""" it would be cool to be provide a "labeling" function which could generate
	the code from a given regex, as part of a debugging suite 
	"""
	pass


def optional(*args):
	return f'(?:{"".join(args)})?'

def capture(*args):
	return f'({"".join(args)})?'

def range(*args):
	character_set = ''
	for arg in args:
		try:
			start, end = arg
			character_set += f'{start}-{end}'
		except:
			raise

	return f'[{character_set}]'

def exactly(length):
	return f'{length}'

def atLeast(length):
	return f'{length},'

def between(minl, maxl):
	return f'{minl},{maxl}'
