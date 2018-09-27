"""
Defines metrics that operate per line.
"""

def indent_level(line):
	result = 0
	for c in line:
		if c.isspace():
			result += 1
		else:
			break
	return result

def ends_with_whitespace(line):
	if len(line) < 1: return False
	return line[len(line)-1].isspace()

default_metrics = [
	{
		'name': 'Indent Level',
		'type': 'int',
		'method': indent_level
	},
	{
		'name': 'Ends With Whitespace',
		'type': 'bool',
		'method': ends_with_whitespace
	},
]
