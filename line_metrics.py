"""
Defines metrics that operate per line.
"""

from stats import Metric

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

default = [
	Metric(
		id='line_length',
		name='Line Length',
		type='int',
		method=len ),
	Metric(
		id='line_indent_level',
		name='Line Indent Level',
		type='int',
		method=indent_level ),
	Metric(
		id='line_exists',
		name='Line Count',
		type='bool',
		method=lambda x: True ),
	Metric(
		id='line_ends_with_whitespace',
		name='Lines Ending in Whitespace',
		type='bool',
		method=ends_with_whitespace ),
]
