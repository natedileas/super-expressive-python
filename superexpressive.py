import re

quantifierTable = {
	"oneOrMore": '+',
	"oneOrMoreLazy": '+?',
	"zeroOrMore": '*',
	"zeroOrMoreLazy": '*?',
	"optional": '?',
	# "exactly": times => `{${times}}`,
	# "atLeast": times => `{${times},}`,
	# "between": times => `{${times[0]},${times[1]}}`,
	# "betweenLazy": times => `{${times[0]},${times[1]}}?`,
}
