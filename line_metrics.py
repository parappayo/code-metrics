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
		'line_length',
		'Line Length',
		'int',
		len ),
	Metric(
		'line_indent_level',
		'Line Indent Level',
		'int',
		indent_level ),
	Metric(
		'line_exists',
		'Line Count',
		'bool',
		lambda x: True ),
	Metric(
		'line_ends_with_whitespace',
		'Lines Ending in Whitespace',
		'bool',
		ends_with_whitespace ),
]
