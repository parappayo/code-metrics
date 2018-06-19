"""
Generates metrics for given source code input.

Command Line:
> python code_metrics.py [file path]
"""

import sys

def ends_with_whitespace(line):
	if len(line) < 1: return False
	return line[len(line)-1].isspace()

def line_count(code):
	return code.count('\n')

def lines_ending_in_whitespace_count(lines):
	return sum(map(ends_with_whitespace, lines))

def distribution(values):
	result = {}
	for value in values:
		if value in result:
			result[value] += 1
		else:
			result[value] = 1
	return result

def line_length_distribution(lines):
	return distribution(map(len, lines))

def line_indent_charlen(line):
	result = 0
	for c in line:
		if c.isspace():
			result += 1
		else:
			break
	return result

def line_indent_distribution(lines):
	return distribution(map(line_indent_charlen, lines))

def report(code):
	lines = code.splitlines()
	return {
		'line_count': line_count(code),
		'lines_ending_in_whitespace_count': lines_ending_in_whitespace_count(lines),
		'line_length_distribution': line_length_distribution(lines),
		'line_indent_distribution': line_indent_distribution(lines)
	}

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print(__doc__)
		#TODO: test() - import code_metrics_test.py
		exit()

	path = sys.argv[1]
	with open(path, "r") as input_file:
		code = input_file.read()
		print(report(code))
